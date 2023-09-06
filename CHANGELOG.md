# Changelog

## 0.11.1 (2023-09-06)

#### Refactorings

- `StallsPosition` as optional `RaceConditions` attr

## 0.11.0 (2023-09-05)

#### New Features

- `Draw` class
- `StallsPosition` enum

## 0.10.2 (2023-08-29)

#### Fixes

- `RaceDistance` handles comma separated int

## 0.10.1 (2023-07-24)

#### Others

- fix method call in `RaceConditions` test

## 0.10.0 (2023-06-15)

#### New Features

- `Going` class
- `RaceConditions` class

## 0.9.2 (2023-06-15)

#### Fixes

- type stubs for `Silks`

## 0.9.1 (2023-06-15)

#### Fixes

- typing in `Silks`

## 0.9.0 (2023-05-25)

#### New Features

- `Silks` class

#### Others

- ruff ignore F821 Undefined name (picks up ParsingEnum members)
- fixture with example silks

## 0.8.2 (2023-05-08)

#### Fixes

- add AW subtypes to `Surface`

#### Others

- add typing stubs

## 0.8.1 (2023-05-08)

#### Refactorings

- `GoingDescription` parent enum

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
