"use client";

export type ChatRole = "user" | "system";

export interface ChatMessage {
  id: string;
  role: ChatRole;
  text: string;
}

interface ChatMessageListProps {
  messages: ChatMessage[];
}

export function ChatMessageList({ messages }: ChatMessageListProps) {
  return (
    <div className="space-y-2 text-sm">
      {messages.map((message) => {
        const isUser = message.role === "user";

        return (
          <div
            key={message.id}
            className={`flex ${isUser ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-[80%] rounded-2xl px-3 py-2 shadow-sm ${
                isUser
                  ? "bg-eco-green text-white"
                  : "bg-white text-stone-800 border border-stone-200"
              }`}
            >
              <p className="whitespace-pre-line">{message.text}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}

