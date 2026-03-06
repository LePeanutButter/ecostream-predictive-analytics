export type TipoVehiculo = "Electrico" | "Diesel" | "Hibrido";

export interface ActividadRequest {
  tipo_vehiculo: TipoVehiculo;
  distancia_km: number;
  peso_toneladas: number;
  factor_eficiencia: number;
}

export interface ResultadoHuellaResponse {
  total_co2e_kg: number;
  total_co2e_ton: number;
  _links: {
    self: { href: string };
    actividades: { href: string };
  };
}

export interface EcoStreamErrorResponse {
  detail: string;
}
