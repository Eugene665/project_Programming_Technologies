import { supabase } from "./supabase";

export async function authenticateUser(login_or_email, password) {
  try {
    const { data, error } = await supabase.rpc("authenticate_user", {
      login_or_email: login_or_email,
      p_password: password,
    });
    if (error) throw error;
    return data;
  } catch (error) {
    throw new Error(error.message);
  }
}

export async function signup(
  email,
  password,
  username,
  isCompanyOrUser,
  about = ""
) {
  try {
    if (!isCompanyOrUser) {
      const { error } = await supabase.rpc("register_user", {
        p_email: email,
        p_password: password,
        p_username: username,
      });
      if (error) throw error;
    } else {
      const { error } = await supabase.rpc("register_company", {
        p_username: username,
        p_password: password,
        p_email: email,
        p_about: about,
      });
      if (error) throw error;
    }
  } catch (error) {
    throw new Error(error.message);
  }
}
