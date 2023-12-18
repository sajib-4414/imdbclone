CREATE TABLE `User` (
  `id` integer,
  `email` string,
  `firstname` string,
  `lastname` string,
  `password` string,
  `is_staff` boolean,
  `role` string,
  `groups` [],
  `permissions` string[]
);

CREATE TABLE `ContentCreatorProfile` (
  `id` integer,
  `user` User,
  `creator_id` string,
  `isPaidMemmber` boolean,
  `paidMembershipValidTill` Datetime
);

CREATE TABLE `RegularProfile` (
  `id` integer,
  `user` User,
  `creator_id` string,
  `isPaidMemmber` boolean,
  `paidMembershipValidTill` Datetime
);

CREATE TABLE `Group` (
  `id` integer,
  `name` string,
  `permissions` Permission[]
);

CREATE TABLE `Permission` (
  `codename` string,
  `description` string
);

CREATE TABLE `StreamingPlatform` (
  `id` integer,
  `name` string,
  `about` string,
  `website` string,
  `logo_url` string
);

CREATE TABLE `ProductionCompany` (
  `id` integer PRIMARY KEY,
  `name` string,
  `description` text,
  `logo_url` string
);

CREATE TABLE `Movie` (
  `id` integer,
  `title` string,
  `storyline` string,
  `platform` StreamingPlatform[],
  `production_company` ProductionCompany,
  `trailer` Trailer,
  `image` Image,
  `active` boolean,
  `avg_rating` float,
  `number_of_ratings` integer,
  `moviePersons` MoviePerson[],
  `comments` [],
  `lengthInMinutes` int
);

CREATE TABLE `TVShow` (
  `id` integer PRIMARY KEY,
  `title` string,
  `storyline` string,
  `active` boolean,
  `avg_rating` float,
  `number_of_ratings` integer,
  `production_company` ProductionCompany,
  `platform` StreamingPlatform,
  `tvShowPersons` TVShowPerson[],
  `trailer` Trailer,
  `image` Image,
  `lengthInMinutes` int
);

CREATE TABLE `Image` (
  `id` integer,
  `source_type` string,
  `source_id` integer,
  `url` string
);

CREATE TABLE `Trailer` (
  `id` integer,
  `source` enum,
  `source_type` string,
  `source_id` integer,
  `url` string
);

CREATE TABLE `Watchlist` (
  `owner` User,
  `movies` Movie[]
);

CREATE TABLE `Review` (
  `review_user` RegularProfile,
  `rating` integer,
  `description` text,
  `active` boolean,
  `movie` Movie,
  `timestamp` datetime,
  `comments` Comment[]
);

CREATE TABLE `Notification` (
  `target_user` User,
  `deeplink_destination` string,
  `text` string,
  `need_email` boolean,
  `emailed` boolean
);

CREATE TABLE `Comment` (
  `id` integer,
  `creator` User,
  `message` string,
  `sent_at` timestampt,
  `parent_comment` integer,
  `source_type` string,
  `source_id` integer
);

CREATE TABLE `Genre` (
  `id` integer,
  `name` string
);

CREATE TABLE `MovieGenre` (
  `id` integer,
  `movie` Movie,
  `genre` Genre
);

CREATE TABLE `TvShowGenre` (
  `id` integer,
  `tvShow` TVShow,
  `genre` Genre
);

CREATE TABLE `MediaPerson` (
  `id` integer PRIMARY KEY,
  `name` string,
  `biography` text,
  `birth_date` date,
  `birth_place` string,
  `image_url` string
);

CREATE TABLE `MoviePerson` (
  `id` integer PRIMARY KEY,
  `movie` Movie,
  `person` MediaPerson,
  `role` string,
  `character_name` string
);

CREATE TABLE `TVShowPerson` (
  `id` integer PRIMARY KEY,
  `tvShow` TVShow,
  `person` MediaPerson,
  `role` string,
  `character_name` string
);

CREATE TABLE `Favorites` (
  `profile` RegularProfile,
  `movies` Movie[],
  `tvShows` tvShow[]
);

CREATE TABLE `Award` (
  `id` integer,
  `name` string
);

CREATE TABLE `MovieAward` (
  `movie` Movie,
  `award` Award,
  `year` integer
);

CREATE TABLE `TVshowAward` (
  `tvShow` TVShow,
  `award` Award,
  `year` integer
);

CREATE TABLE `Viewed` (
  `profile` RegularProfile,
  `content_id` integer,
  `content_type` string,
  `timestamp` datetime
);

ALTER TABLE `User` ADD FOREIGN KEY (`id`) REFERENCES `Review` (`review_user`);

ALTER TABLE `Review` ADD FOREIGN KEY (`movie`) REFERENCES `Movie` (`id`);

CREATE TABLE `Movie_StreamingPlatform` (
  `Movie_platform` StreamingPlatform[],
  `StreamingPlatform_id` integer,
  PRIMARY KEY (`Movie_platform`, `StreamingPlatform_id`)
);

ALTER TABLE `Movie_StreamingPlatform` ADD FOREIGN KEY (`Movie_platform`) REFERENCES `Movie` (`platform`);

ALTER TABLE `Movie_StreamingPlatform` ADD FOREIGN KEY (`StreamingPlatform_id`) REFERENCES `StreamingPlatform` (`id`);


CREATE TABLE `TVShow_StreamingPlatform` (
  `TVShow_platform` StreamingPlatform,
  `StreamingPlatform_id` integer,
  PRIMARY KEY (`TVShow_platform`, `StreamingPlatform_id`)
);

ALTER TABLE `TVShow_StreamingPlatform` ADD FOREIGN KEY (`TVShow_platform`) REFERENCES `TVShow` (`platform`);

ALTER TABLE `TVShow_StreamingPlatform` ADD FOREIGN KEY (`StreamingPlatform_id`) REFERENCES `StreamingPlatform` (`id`);


CREATE TABLE `Movie_ProductionCompany` (
  `Movie_production_company` ProductionCompany,
  `ProductionCompany_id` integer,
  PRIMARY KEY (`Movie_production_company`, `ProductionCompany_id`)
);

ALTER TABLE `Movie_ProductionCompany` ADD FOREIGN KEY (`Movie_production_company`) REFERENCES `Movie` (`production_company`);

ALTER TABLE `Movie_ProductionCompany` ADD FOREIGN KEY (`ProductionCompany_id`) REFERENCES `ProductionCompany` (`id`);


ALTER TABLE `Notification` ADD FOREIGN KEY (`target_user`) REFERENCES `User` (`id`);

ALTER TABLE `Comment` ADD FOREIGN KEY (`creator`) REFERENCES `User` (`id`);

ALTER TABLE `User` ADD FOREIGN KEY (`id`) REFERENCES `Watchlist` (`owner`);

ALTER TABLE `Movie` ADD FOREIGN KEY (`id`) REFERENCES `Watchlist` (`movies`);

CREATE TABLE `User_Group` (
  `User_groups` [],
  `Group_id` integer,
  PRIMARY KEY (`User_groups`, `Group_id`)
);

ALTER TABLE `User_Group` ADD FOREIGN KEY (`User_groups`) REFERENCES `User` (`groups`);

ALTER TABLE `User_Group` ADD FOREIGN KEY (`Group_id`) REFERENCES `Group` (`id`);


ALTER TABLE `Movie` ADD FOREIGN KEY (`id`) REFERENCES `MovieGenre` (`movie`);

ALTER TABLE `Genre` ADD FOREIGN KEY (`id`) REFERENCES `MovieGenre` (`genre`);

ALTER TABLE `Genre` ADD FOREIGN KEY (`id`) REFERENCES `TvShowGenre` (`genre`);

CREATE TABLE `Permission_Group` (
  `Permission_codename` string,
  `Group_id` integer,
  PRIMARY KEY (`Permission_codename`, `Group_id`)
);

ALTER TABLE `Permission_Group` ADD FOREIGN KEY (`Permission_codename`) REFERENCES `Permission` (`codename`);

ALTER TABLE `Permission_Group` ADD FOREIGN KEY (`Group_id`) REFERENCES `Group` (`id`);


ALTER TABLE `Image` ADD FOREIGN KEY (`id`) REFERENCES `Movie` (`image`);

ALTER TABLE `Trailer` ADD FOREIGN KEY (`id`) REFERENCES `Movie` (`trailer`);

ALTER TABLE `Image` ADD FOREIGN KEY (`id`) REFERENCES `TVShow` (`image`);

ALTER TABLE `Trailer` ADD FOREIGN KEY (`id`) REFERENCES `TVShow` (`trailer`);

ALTER TABLE `MoviePerson` ADD FOREIGN KEY (`id`) REFERENCES `Movie` (`moviePersons`);

ALTER TABLE `TVShowPerson` ADD FOREIGN KEY (`id`) REFERENCES `TVShow` (`tvShowPersons`);

ALTER TABLE `MoviePerson` ADD FOREIGN KEY (`id`) REFERENCES `MediaPerson` (`id`);

ALTER TABLE `TVShowPerson` ADD FOREIGN KEY (`id`) REFERENCES `MediaPerson` (`id`);

ALTER TABLE `Comment` ADD FOREIGN KEY (`id`) REFERENCES `Movie` (`id`);

CREATE TABLE `Favorites_Movie` (
  `Favorites_movies` Movie[],
  `Movie_id` integer,
  PRIMARY KEY (`Favorites_movies`, `Movie_id`)
);

ALTER TABLE `Favorites_Movie` ADD FOREIGN KEY (`Favorites_movies`) REFERENCES `Favorites` (`movies`);

ALTER TABLE `Favorites_Movie` ADD FOREIGN KEY (`Movie_id`) REFERENCES `Movie` (`id`);


CREATE TABLE `Favorites_TVShow` (
  `Favorites_tvShows` tvShow[],
  `TVShow_id` integer,
  PRIMARY KEY (`Favorites_tvShows`, `TVShow_id`)
);

ALTER TABLE `Favorites_TVShow` ADD FOREIGN KEY (`Favorites_tvShows`) REFERENCES `Favorites` (`tvShows`);

ALTER TABLE `Favorites_TVShow` ADD FOREIGN KEY (`TVShow_id`) REFERENCES `TVShow` (`id`);


CREATE TABLE `Favorites_RegularProfile` (
  `Favorites_profile` RegularProfile,
  `RegularProfile_id` integer,
  PRIMARY KEY (`Favorites_profile`, `RegularProfile_id`)
);

ALTER TABLE `Favorites_RegularProfile` ADD FOREIGN KEY (`Favorites_profile`) REFERENCES `Favorites` (`profile`);

ALTER TABLE `Favorites_RegularProfile` ADD FOREIGN KEY (`RegularProfile_id`) REFERENCES `RegularProfile` (`id`);


CREATE TABLE `RegularProfile_User` (
  `RegularProfile_user` User,
  `User_id` integer,
  PRIMARY KEY (`RegularProfile_user`, `User_id`)
);

ALTER TABLE `RegularProfile_User` ADD FOREIGN KEY (`RegularProfile_user`) REFERENCES `RegularProfile` (`user`);

ALTER TABLE `RegularProfile_User` ADD FOREIGN KEY (`User_id`) REFERENCES `User` (`id`);


CREATE TABLE `ContentCreatorProfile_User` (
  `ContentCreatorProfile_user` User,
  `User_id` integer,
  PRIMARY KEY (`ContentCreatorProfile_user`, `User_id`)
);

ALTER TABLE `ContentCreatorProfile_User` ADD FOREIGN KEY (`ContentCreatorProfile_user`) REFERENCES `ContentCreatorProfile` (`user`);

ALTER TABLE `ContentCreatorProfile_User` ADD FOREIGN KEY (`User_id`) REFERENCES `User` (`id`);


ALTER TABLE `Award` ADD FOREIGN KEY (`id`) REFERENCES `MovieAward` (`movie`);

ALTER TABLE `Award` ADD FOREIGN KEY (`id`) REFERENCES `TVshowAward` (`tvShow`);

ALTER TABLE `Movie` ADD FOREIGN KEY (`id`) REFERENCES `MovieAward` (`movie`);

ALTER TABLE `TVShow` ADD FOREIGN KEY (`id`) REFERENCES `TVshowAward` (`tvShow`);

ALTER TABLE `RegularProfile` ADD FOREIGN KEY (`id`) REFERENCES `Viewed` (`profile`);
