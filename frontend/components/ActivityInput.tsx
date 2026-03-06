"use client";

import { useState } from "react";
import { Leaf } from "lucide-react";
import { calcularHuella } from "@/services/api";
import type { ActividadRequest, ResultadoHuellaResponse } from "@/types/ecostream";
import { ApiError } from "@/services/api";
import { ResultCard } from "./ResultCard";
import { LoadingState } from "./LoadingState";
import { ErrorMessage } from "./ErrorMessage";

type ApiState = "idle" | "loading" | "success" | "error";

const TIPOS_VEHICULO: { value: ActividadRequest["tipo_vehiculo"]; label: string }[] = [
  { value: "Diesel", label: "Diesel" },
  { value: "Electrico", label: "Eléctrico" },
  { value: "Hibrido", label: "Híbrido" },
];

export function ActivityInput() {
  const [state, setState] = useState<ApiState>("idle");
  const [result, setResult] = useState<ResultadoHuellaResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [form, setForm] = useState<ActividadRequest>({
    tipo_vehiculo: "Diesel",
    distancia_km: 0,
    peso_toneladas: 1,
    factor_eficiencia: 1,
  });

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setState("loading");
    setError(null);
    setResult(null);
    try {
      const data = await calcularHuella(form);
      setResult(data);
      setState("success");
    } catch (e) {
      const msg = e instanceof ApiError ? e.detail ?? e.message : "Error al calcular huella";
      setError(msg);
      setState("error");
    }
  }

  return (
    <div className="space-y-6">
      <form onSubmit={handleSubmit} className="rounded-xl border border-stone-200 bg-white p-6 shadow-sm">
        <div className="grid gap-4 sm:grid-cols-2">
          <div>
            <label htmlFor="tipo_vehiculo" className="mb-1 block text-sm font-medium text-stone-700">
              Tipo de vehículo
            </label>
            <select
              id="tipo_vehiculo"
              value={form.tipo_vehiculo}
              onChange={(e) =>
                setForm((f) => ({ ...f, tipo_vehiculo: e.target.value as ActividadRequest["tipo_vehiculo"] }))
              }
              className="w-full rounded-lg border border-stone-300 px-3 py-2 text-stone-800 focus:border-eco-green focus:outline-none focus:ring-1 focus:ring-eco-green"
            >
              {TIPOS_VEHICULO.map((t) => (
                <option key={t.value} value={t.value}>
                  {t.label}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="distancia_km" className="mb-1 block text-sm font-medium text-stone-700">
              Distancia (km)
            </label>
            <input
              id="distancia_km"
              type="number"
              min={0}
              step={0.1}
              value={form.distancia_km || ""}
              onChange={(e) =>
                setForm((f) => ({ ...f, distancia_km: parseFloat(e.target.value) || 0 }))
              }
              className="w-full rounded-lg border border-stone-300 px-3 py-2 text-stone-800 focus:border-eco-green focus:outline-none focus:ring-1 focus:ring-eco-green"
            />
          </div>
          <div>
            <label htmlFor="peso_toneladas" className="mb-1 block text-sm font-medium text-stone-700">
              Peso (toneladas)
            </label>
            <input
              id="peso_toneladas"
              type="number"
              min={0.01}
              step={0.1}
              value={form.peso_toneladas || ""}
              onChange={(e) =>
                setForm((f) => ({ ...f, peso_toneladas: parseFloat(e.target.value) || 1 }))
              }
              className="w-full rounded-lg border border-stone-300 px-3 py-2 text-stone-800 focus:border-eco-green focus:outline-none focus:ring-1 focus:ring-eco-green"
            />
          </div>
          <div>
            <label htmlFor="factor_eficiencia" className="mb-1 block text-sm font-medium text-stone-700">
              Factor de eficiencia
            </label>
            <input
              id="factor_eficiencia"
              type="number"
              min={0.01}
              step={0.01}
              value={form.factor_eficiencia || ""}
              onChange={(e) =>
                setForm((f) => ({ ...f, factor_eficiencia: parseFloat(e.target.value) || 1 }))
              }
              className="w-full rounded-lg border border-stone-300 px-3 py-2 text-stone-800 focus:border-eco-green focus:outline-none focus:ring-1 focus:ring-eco-green"
            />
          </div>
        </div>
        <button
          type="submit"
          disabled={state === "loading"}
          className="mt-6 flex w-full items-center justify-center gap-2 rounded-lg bg-eco-green px-4 py-3 font-medium text-white transition hover:bg-eco-dark disabled:opacity-50"
        >
          <Leaf className="h-5 w-5" />
          Calcular huella
        </button>
      </form>

      {state === "loading" && <LoadingState />}
      {state === "error" && error && <ErrorMessage message={error} />}
      {state === "success" && result && <ResultCard result={result} />}
    </div>
  );
}
