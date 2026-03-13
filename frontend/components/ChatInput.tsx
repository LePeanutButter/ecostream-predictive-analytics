"use client";

import { useCallback } from "react";

interface ChatInputProps {
  value: string;
  onChange: (value: string) => void;
  onSend: (message: string) => void;
  disabled?: boolean;
}

export function ChatInput({ value, onChange, onSend, disabled }: ChatInputProps) {
  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      if (!value.trim() || disabled) return;
      onSend(value);
    },
    [value, disabled, onSend],
  );

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        if (!value.trim() || disabled) return;
        onSend(value);
      }
    },
    [value, disabled, onSend],
  );

  return (
    <form onSubmit={handleSubmit} className="space-y-2">
      <textarea
        rows={3}
        className="w-full resize-none rounded-lg border border-stone-300 px-3 py-2 text-sm text-stone-800 focus:border-eco-green focus:outline-none focus:ring-1 focus:ring-eco-green disabled:bg-stone-100"
        placeholder="Describe aquí tu actividad de transporte..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onKeyDown={handleKeyDown}
        disabled={disabled}
      />
      <div className="flex justify-end">
        <button
          type="submit"
          disabled={disabled || !value.trim()}
          className="inline-flex items-center rounded-lg bg-eco-green px-4 py-2 text-sm font-medium text-white transition hover:bg-eco-dark disabled:opacity-50"
        >
          Enviar
        </button>
      </div>
    </form>
  );
}

