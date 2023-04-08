# Changelog

## 0.5.0 (2023-04-08)

#### New Features

- `FormFigures` class with `parse` method
- `FormBreak` enum
- `FinishingPosition` enum
- `Headgear` enum
- `JockeyExperience` enum
- add ROAN to `CoatColour`
- add AUCTION, CLAIMER, SELLER to `RaceDesignation`

#### Refactorings

- `WeightDeterminant` -> `RaceDesignation`
- `ExperienceLevel` -> `HorseExperienceLevel`
- `FormFigures.parse` now uses list comprehension

#### Others

- rename tests correctly

## 0.4.0 (2023-04-08)

#### New Features

- `AgeCategory` enum
- `ExperienceLevel` enum
- `WeightDeterminant` enum
- `RaceTitle` class with `parse` function, handling `AgeCategory`, `ExperienceLevel`, `Gender`, `Obstacle`, `WeightDeterminant` and name
- `ParsingEnum` made apostrophe neutral

## 0.3.0 (2023-04-07)

#### New Features

- `RacingCode` enum
- `Surface` enum
- `AWGoingDescription` enum
- `DirtGoingDescription` enum
- `TurfGoingDescription` enum

#### Refactorings

- create `ParsingEnum` base

#### Others

- ignore line too long warning E501

## 0.2.0 (2023-04-06)

#### New Features

- `Disaster` enum
- `Obstacle` enum

#### Docs

- missing docstring on `Gender`

#### Others

- ignore ambiguous variable warning E741

## 0.1.0 (2023-04-06)

#### New Features

- `Breed` enum
- `CoatColour` enum
- `Gender` enum
- `Sex` enum

#### Others

- `poetry` and base packages
