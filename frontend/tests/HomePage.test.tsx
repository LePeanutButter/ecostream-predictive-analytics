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

  it("renderiza el botón de calcular huella", () => {
    render(<HomePage />);
    expect(screen.getByRole("button", { name: /Calcular huella/i })).toBeInTheDocument();
  });

  it("renderiza el formulario con campos de actividad", () => {
    render(<HomePage />);
    expect(screen.getByLabelText(/Tipo de vehículo/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Distancia \(km\)/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Peso \(toneladas\)/i)).toBeInTheDocument();
    expect(screen.getByLabelText(/Factor de eficiencia/i)).toBeInTheDocument();
  });
});
