const getApiBaseUrl = () => {
  if (typeof window !== "undefined") {
    // En el navegador, si estamos en un subdominio de replit, el backend está en el mismo host pero puerto 8000
    // Sin embargo, en Replit, los puertos se mapean a subdominios.
    // La forma más fiable es usar la variable de entorno o construirla.
    const replitDomain = process.env.NEXT_PUBLIC_REPLIT_DEV_DOMAIN;
    if (replitDomain) {
      return `https://${replitDomain.replace("-00-", "-8000-")}`;
    }
  }
  return process.env.NEXT_PUBLIC_ECOSTREAM_URL ?? "http://localhost:8000";
};

export const API_BASE_URL = getApiBaseUrl();
