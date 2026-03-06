import { calcularHuella, checkHealth, ApiError } from "@/services/api";

const originalFetch = globalThis.fetch;

beforeEach(() => {
  globalThis.fetch = originalFetch;
});

describe("checkHealth", () => {
  it("devuelve { status: 'ok' } cuando la API responde 200", async () => {
    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: true,
      json: async () => ({ status: "ok" }),
    });

    const result = await checkHealth();
    expect(result).toEqual({ status: "ok" });
    expect(fetch).toHaveBeenCalledWith(
      expect.stringMatching(/\/api\/health$/),
      undefined
    );
  });

  it("lanza ApiError cuando la API responde con error", async () => {
    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: false,
      status: 500,
      statusText: "Internal Server Error",
      json: async () => ({ detail: "Error interno del servidor" }),
    });

    await expect(checkHealth()).rejects.toThrow(ApiError);
  });

  it("ApiError incluye detail del backend", async () => {
    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: false,
      status: 500,
      json: async () => ({ detail: "Error interno del servidor" }),
    });
    try {
      await checkHealth();
    } catch (e) {
      expect(e).toBeInstanceOf(ApiError);
      expect((e as ApiError).detail).toBe("Error interno del servidor");
    }
  });
});

describe("calcularHuella", () => {
  it("devuelve ResultadoHuellaResponse cuando la API responde 201", async () => {
    const mockResponse = {
      total_co2e_kg: 268,
      total_co2e_ton: 0.268,
      _links: { self: { href: "/api/resultado-huella" }, actividades: { href: "/api/actividades" } },
    };

    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: true,
      json: async () => mockResponse,
    });

    const payload = {
      tipo_vehiculo: "Diesel" as const,
      distancia_km: 100,
      peso_toneladas: 1,
      factor_eficiencia: 1,
    };

    const result = await calcularHuella(payload);
    expect(result).toEqual(mockResponse);
    expect(fetch).toHaveBeenCalledWith(
      expect.stringMatching(/\/api\/resultado-huella$/),
      expect.objectContaining({
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      })
    );
  });

  it("lanza ApiError con detail cuando la API responde 400", async () => {
    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: false,
      status: 400,
      statusText: "Bad Request",
      json: async () => ({ detail: "Vehículo InvalidType no soportado" }),
    });

    await expect(
      calcularHuella({
        tipo_vehiculo: "Diesel",
        distancia_km: 100,
        peso_toneladas: 1,
        factor_eficiencia: 1,
      })
    ).rejects.toThrow(ApiError);
  });

  it("ApiError de calcularHuella incluye detail", async () => {
    globalThis.fetch = jest.fn().mockResolvedValueOnce({
      ok: false,
      status: 400,
      json: async () => ({ detail: "Vehículo InvalidType no soportado" }),
    });
    try {
      await calcularHuella({
        tipo_vehiculo: "Diesel",
        distancia_km: 100,
        peso_toneladas: 1,
        factor_eficiencia: 1,
      });
    } catch (e) {
      expect(e).toBeInstanceOf(ApiError);
      expect((e as ApiError).detail).toBe("Vehículo InvalidType no soportado");
    }
  });
});
