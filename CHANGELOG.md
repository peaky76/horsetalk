# Changelog

## 0.8.0 (2023-04-13)

#### New Features

- `ObstacleStyle` enum

#### Fixes

- remove deleted `RaceExperienceStatus` class from `__init__`

#### Refactorings

- rename `Obstacle` to `JumpCategory`

#### Docs

- remove duplicate text in CHANGELOG

## 0.7.0 (2023-04-13)

#### New Features

- `Gender.sex` property
- `Gender.determine` method from `Sex` and age args
- `Disaster.is_jumping/behavioural/third_party_error` properties

#### Docs

- fill out missing docstrings, format others

## 0.6.1 (2023-04-08)

#### Fixes

- `ParsingEnum` trims whitespace

## 0.6.0 (2023-04-08)

#### New Features

- `HorseAge` class
- `HorseHeight` class
- `Horselength` class
- `RaceDistance` class

#### Others

- add pytest-mock to dev deps
- add pendulum

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
