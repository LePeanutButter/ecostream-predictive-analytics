"use client";

import { Leaf } from "lucide-react";
import type { ResultadoHuellaResponse } from "@/types/ecostream";

interface ResultCardProps {
  result: ResultadoHuellaResponse;
}

export function ResultCard({ result }: ResultCardProps) {
  return (
    <div className="rounded-xl border border-eco-light bg-eco-light/30 p-6 shadow-sm">
      <div className="flex items-center gap-2 text-eco-dark">
        <Leaf className="h-6 w-6" />
        <h2 className="text-lg font-semibold">Resultado de huella de carbono</h2>
      </div>
      <div className="mt-4 grid gap-2 sm:grid-cols-2">
        <div className="rounded-lg bg-white/80 p-4">
          <p className="text-sm text-stone-600">CO₂e (kg)</p>
          <p className="text-2xl font-bold text-eco-dark">
            {result.total_co2e_kg.toLocaleString("es", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
          </p>
        </div>
        <div className="rounded-lg bg-white/80 p-4">
          <p className="text-sm text-stone-600">CO₂e (ton)</p>
          <p className="text-2xl font-bold text-eco-dark">
            {result.total_co2e_ton.toLocaleString("es", { minimumFractionDigits: 4, maximumFractionDigits: 6 })}
          </p>
        </div>
      </div>
    </div>
  );
}
