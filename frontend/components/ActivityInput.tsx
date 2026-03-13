"use client";

import { useState } from "react";
import { Leaf } from "lucide-react";
import {
  ApiError,
  calcularHuellaDesdeTexto,
  type ChatResultadoResponse,
} from "@/services/api";
import type { ResultadoHuellaResponse } from "@/types/ecostream";
import { LoadingState } from "./LoadingState";
import { ErrorMessage } from "./ErrorMessage";
import { ResultCard } from "./ResultCard";
import { ChatMessageList, type ChatMessage } from "./ChatMessageList";
import { ChatInput } from "./ChatInput";

type ApiState = "idle" | "loading" | "success" | "error";

export function ActivityInput() {
  const [state, setState] = useState<ApiState>("idle");
  const [result, setResult] = useState<ResultadoHuellaResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [inputValue, setInputValue] = useState("");
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: "welcome",
      role: "system",
      text: "Describe tu actividad de transporte (por ejemplo: 'Hoy usamos 5 camionetas de reparto y recorrimos 200 km con 10 toneladas de carga').",
    },
  ]);

  async function handleSendMessage(text: string) {
    const trimmed = text.trim();
    if (!trimmed || state === "loading") return;

    setInputValue("");
    setError(null);
    setResult(null);
    setState("loading");

    const userMessage: ChatMessage = {
      id: `user-${Date.now()}`,
      role: "user",
      text: trimmed,
    };

    const loadingMessage: ChatMessage = {
      id: "loading",
      role: "system",
      text: "Analizando tu actividad...",
    };

    setMessages((prev) => [...prev, userMessage, loadingMessage]);

    try {
      const data: ChatResultadoResponse = await calcularHuellaDesdeTexto(trimmed);
      setResult(data);
      setState("success");

      setMessages((prev) =>
        prev.map((m) =>
          m.id === "loading" ? { ...m, text: data.result_text } : m,
        ),
      );
    } catch (e) {
      const msg =
        e instanceof ApiError ? e.detail ?? e.message : "Error al calcular huella";
      setError(msg);
      setState("error");

      setMessages((prev) =>
        prev.map((m) =>
          m.id === "loading"
            ? { ...m, text: `Ocurrió un error al analizar la actividad: ${msg}` }
            : m,
        ),
      );
    }
  }

  return (
    <div className="space-y-6">
      <div className="rounded-xl border border-stone-200 bg-white p-6 shadow-sm">
        <div className="mb-4 flex items-center gap-2">
          <Leaf className="h-5 w-5 text-eco-green" />
          <h2 className="text-lg font-semibold text-eco-dark">
            Describe tu actividad de transporte
          </h2>
        </div>

        <div className="mb-4 h-64 space-y-3 overflow-y-auto rounded-lg border border-stone-100 bg-stone-50 p-3">
          <ChatMessageList messages={messages} />
        </div>

        <ChatInput
          value={inputValue}
          onChange={setInputValue}
          onSend={handleSendMessage}
          disabled={state === "loading"}
        />
      </div>

      {state === "loading" && <LoadingState />}
      {state === "error" && error && <ErrorMessage message={error} />}
      {state === "success" && result && <ResultCard result={result} />}
    </div>
  );
}