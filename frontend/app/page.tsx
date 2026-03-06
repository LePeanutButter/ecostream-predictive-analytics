import { ActivityInput } from "@/components/ActivityInput";

export default function HomePage() {
  return (
    <main className="mx-auto max-w-2xl px-4 py-12">
      <header className="mb-10 text-center">
        <h1 className="text-3xl font-bold text-eco-dark">EcoTrack</h1>
        <p className="mt-2 text-stone-600">
          Estima la huella de carbono de tu actividad de transporte
        </p>
      </header>
      <ActivityInput />
    </main>
  );
}
