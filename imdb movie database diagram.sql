CREATE TABLE [User] (
  [id] integer,
  [email] string,
  [firstname] string,
  [lastname] string,
  [password] string,
  [is_staff] boolean
)
GO

CREATE TABLE [StreamingPlatform] (
  [id] integer,
  [name] string,
  [about] string,
  [website] string
)
GO

CREATE TABLE [Movie] (
  [id] integer,
  [title] string,
  [storyline] string,
  [platform] StreamingPlatform,
  [active] boolean,
  [avg_rating] float,
  [number_of_ratings] integer
)
GO

CREATE TABLE [Watchlist] (
  [owner] User,
  [movies] Movie[]
)
GO

CREATE TABLE [Review] (
  [review_user] User,
  [rating] integer,
  [description] text,
  [active] boolean,
  [movie] Movie
)
GO

CREATE TABLE [Notification] (
  [target_user] User,
  [destination] string,
  [text] string
)
GO

CREATE TABLE [Comment] (
  [creator] User,
  [message] string,
  [sent_at] timestampt,
  [parent_comment] integer,
  [source_movie] Movie,
  [soure_review] Review
)
GO

ALTER TABLE [User] ADD FOREIGN KEY ([id]) REFERENCES [Review] ([review_user])
GO

ALTER TABLE [Review] ADD FOREIGN KEY ([movie]) REFERENCES [Movie] ([id])
GO

ALTER TABLE [StreamingPlatform] ADD FOREIGN KEY ([id]) REFERENCES [Movie] ([platform])
GO

ALTER TABLE [Notification] ADD FOREIGN KEY ([target_user]) REFERENCES [User] ([id])
GO

ALTER TABLE [Comment] ADD FOREIGN KEY ([creator]) REFERENCES [User] ([id])
GO

ALTER TABLE [User] ADD FOREIGN KEY ([id]) REFERENCES [Watchlist] ([owner])
GO

ALTER TABLE [Movie] ADD FOREIGN KEY ([id]) REFERENCES [Watchlist] ([movies])
GO
