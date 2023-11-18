export interface LoggedInUser {
  id: number;
  // name: string; will be brought soon
  email: string;
  username: string;
  token: string;
  refresh_token: string;
}

export interface LoggedInUserState {
  loggedInUser: LoggedInUser | null;
}
