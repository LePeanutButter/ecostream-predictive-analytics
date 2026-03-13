import { render, screen } from "@testing-library/react";
import HomePage from "@/app/page";

describe("HomePage", () => {
  it("renderiza el título EcoTrack", () => {
    render(<HomePage />);
    expect(screen.getByRole("heading", { name: /EcoTrack/i })).toBeInTheDocument();
  });

  it("renderiza la descripción de la aplicación", () => {
    render(<HomePage />);
    expect(
      screen.getByText(/Estima la huella de carbono de tu actividad de transporte/i)
    ).toBeInTheDocument();
  });

  it("renderiza el botón de enviar del chat", () => {
    render(<HomePage />);
    expect(screen.getByRole("button", { name: /Enviar/i })).toBeInTheDocument();
  });

  it("renderiza el input de texto del chat", () => {
    render(<HomePage />);
    expect(
      screen.getByPlaceholderText(/Describe aquí tu actividad de transporte.../i)
    ).toBeInTheDocument();
  });
});
