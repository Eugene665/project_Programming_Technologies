import { createClient } from "@supabase/supabase-js";

export const supabase = createClient(
  "https://ktgmzsriglttmczagbfc.supabase.co",
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt0Z216c3JpZ2x0dG1jemFnYmZjIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTczNDM2MzkzNiwiZXhwIjoyMDQ5OTM5OTM2fQ.PhSMI4d_8W7B6I2mdj2RXymYh2rGYNnPlXqCzlaJJdY"
);
