"use client";

export function LoadingState() {
  return (
    <div className="flex flex-col items-center justify-center rounded-xl border border-stone-200 bg-stone-50 py-12">
      <div className="h-10 w-10 animate-spin rounded-full border-2 border-eco-green border-t-transparent" />
      <p className="mt-3 text-sm text-stone-600">Calculando huella de carbono...</p>
    </div>
  );
}
