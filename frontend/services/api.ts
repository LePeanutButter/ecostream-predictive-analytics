import { API_BASE_URL } from "@/lib/env";
import type { ActividadRequest, ResultadoHuellaResponse } from "@/types/ecostream";

export class ApiError extends Error {
  constructor(
    message: string,
    public status?: number,
    public detail?: string
  ) {
    super(message);
    this.name = "ApiError";
  }
}

async function parseApiError(response: Response): Promise<ApiError> {
  let detail = "Error al conectar con el servidor";
  try {
    const body = await response.json();
    if (body && typeof body.detail === "string") detail = body.detail;
  } catch {
    detail = response.statusText || detail;
  }
  return new ApiError(detail, response.status, detail);
}

export async function calcularHuella(
  actividad: ActividadRequest
): Promise<ResultadoHuellaResponse> {
  const res = await fetch(`${API_BASE_URL}/api/resultado-huella`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(actividad),
  });
  if (!res.ok) throw await parseApiError(res);
  return res.json();
}

export async function checkHealth(): Promise<{ status: string }> {
  const res = await fetch(`${API_BASE_URL}/api/health`);
  if (!res.ok) throw await parseApiError(res);
  return res.json();
}
