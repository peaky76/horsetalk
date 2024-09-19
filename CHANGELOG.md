# Changelog

## 0.24.0 (2024-09-19)

#### New Features

* `Hemisphere` enum
* `HorseAge` handles different hemispheres

#### Fixes

* typing in `Horse`

## 0.23.3 (2024-09-10)

#### Build

* set locale in ci workflow

## 0.23.2 (2024-04-04)

#### Fixes

- make RacePerformance sortable by Outcome

## 0.23.1 (2024-04-01)

#### Fixes

- allow full unit names in `RaceDistance`
- add sharp as alias for tight in `RacecourseStyle`

#### Docs

- doc status badge
- fix repo size badge

## 0.23.0 (2024-02-24)

#### New Features

- `Horse.breed` attribute

#### Fixes

- `RaceLevel` handles `Listed`

#### Docs

- `Horse` docstrings
- doctest block formatting

#### Others

- run `pre-commit` docs step on any .py file change
- add `sphinx napoleon` extension

## 0.22.4 (2024-02-15)

#### Refactorings

- allow multiple `RaceDesignation`s in `RaceTitle`
- make `HorseAge.date_of_birth` public

#### Docs

- index and api pages

#### Others

- add docs gen as pre-commit hook

## 0.22.3 (2024-02-09)

#### Fixes

- `AgeRestriction` handles non-matching input
- `Horse` init correctly parses multi-word horse names
- `RacePerformance.beaten_distance` handles zero
- type ignores for complex subclasses

#### Refactorings

- `Horse.context_date` as kwarg
- `RacePerformance.time` kwarg
- extra_attributes on `Quantity` subclass

#### Tests

- complete coverage for RaceGrade
- complete coverage for RaceClass

#### Others

- add and configure `pre-commit`
- add `babel` dev dependency
- move and regen type hints, include in build
- ruff lint namespacing in config

## 0.22.2 (2024-01-29)

#### Fixes

- make `RaceClass` hashable
- make `RaceConditions` hashable
- make `RaceGrade` hashable
- make `RaceLevel` hashable
- correct args on `Going` hash

## 0.22.1 (2024-01-25)

#### Fixes

- handle additional format of `Going.multiparse`

#### Build

- add `codspeed`
- relabel and format `dobby`, `vfmn`

## 0.22.0 (2024-01-18)

#### New Features

- `HorsetalkQuantity` parent class

#### Refactorings

- use `pint` library in place of `measurement`
- `HorseHeight` adapted to use `pint` and `HorsetalkQuantity`
- `RaceDistance` adapted to use `pint` and `HorsetalkQuantity`
- `RaceWeight` adapted to use `pint` and `HorsetalkQuantity`

#### Docs

- add Github repo size badge

#### Build

- add `pint`
- remove `measurement`

## 0.21.2 (2024-01-11)

#### Refactorings

- apply fix for RUF012 in race_title
- apply fix for RUF012 in race_grade
- apply fix for PYI041
- apply fixes for FBT
- `ruff` formatting

#### Build

- add `dobby`
- add `version-forget-me-not workflow`

## 0.21.1 (2024-01-02)

#### Fixes

- `RaceGrade.__ne__` implementation
- `RaceClass.__ne__` implementation
- `RaceClass.__eq__` should compare >4 and not compare `RaceGrade` as int
- replace default context_date with conditional in `Horse` to facilitate mocking of `pendulum.now`

#### Refactorings

- apply fixes for `SIM201`
- flip yoda comparison in most tests
- apply fixes for `PT004` and `PT013`
- apply fixes for `N806`
- apply fixes for `RET505`
- swap lambda for def
- `ruff` formatting

#### Docs

- github last commit badge
- remove black badge

#### Tests

- add additional `HorseAge` tests
- remove unneeded mocks in `Horse` tests

#### Build

- add preview to `ruff` lint run
- add `maturin` to ci
- allow more python versions and matrix test them
- lock python version
- remove type ignores from `pytest` and `pendulum`
- remove `black`

## 0.21.0 (2023-10-11)

#### New Features

- `Horse` class
- `Going.multiparse` method

#### Refactorings

- make `RaceConditions` a dataclass
- `Going.**eq**`
- `Going.**hash**`

#### Tests

- flip expected and actual in `Going` tests
- is None for == None in `Age Category` test

## 0.20.0 (2023-10-06)

#### New Features

- `RaceWeight` class

#### Fixes

- `RaceDistance` can be initialised like `measurements.measures.Distance`

#### Refactorings

- `RaceDistance.REGEX` revised
- `RaceDistance.__init__` using `REGEX`

#### Docs

- correct `**repr**` docs for `RaceDistance`, `RaceWeight`

#### Tests

- switch expected and actual in `RaceDistance`
- reorder and rename `RaceDistance` and `RaceWeight` tests

## 0.19.3 (2023-10-06)

#### Refactorings

- typing in `RaceGrade.__init__`
- avoid reassigning `grade_value` in `Outcome` for type safety
- assert not `str` before `Outcome._value` assignment for type safety
- type safety on `RacePerformance.is_official_win`

#### Build

- regen type stubs
- add type ignores

#### Tests

- test for `Outcome.__init__` with invalid str

## 0.19.2 (2023-10-02)

#### Build

- unlock peak-utility until next major version

## 0.19.1 (2023-10-02)

#### Build

- release upper bound on `peak-utility` minor version

#### Tests

- `RaceGrade` not possible with `RacingCode.POINT_TO_POINT`

## 0.19.0 (2023-09-24)

#### New Features

- `FinishingPosition.parse`
- `FinishingPosition` tied position attribute
- `Disaster` enum `REFUSED_TO_RACE`

#### Fixes

- `RaceGrade.__repr__`

#### Refactorings

- `Draw` as RepresentationalInt subclass
- `RaceClass` as RepresentationalInt subclass
- `RaceGrade.PHRASES` dict
- `RaceGrade` as RepresentationalInt subclass
- unneeded `int` cast in `FormFigures`

#### Docs

- docs for `RaceClass`, `RaceGrade` and `RaceLevel`

#### Others

- clarify typing on `Outcome.__init__`
- add missing test for `RaceClass/RaceGrade.__eq__` v objects
- add missing test for `Outcome.__lt__` between `FinishingPositions`
- add missing test for `Horselength.__str__` for whole num

## 0.18.0 (2023-09-20)

#### New Features

- `RacePerformance.beaten_distance` attribute

#### Fixes

- `RaceGrade.__eq__` with `int`

#### Refactorings

- `RaceLevel.__init__` handles more varied input
- `RaceClass.__init__` handles more varied strings
- `RaceGrade.__init__` handles more varied strings

#### Tests

- `Horselength` can be init with `Horselength`
- `RaceClass.__eq__` with int

## 0.17.0 (2023-09-19)

#### New Features

- `Outcome.is_completion`
- `Outcome.is_win`
- `RacePerformance.is_official_win`
- `RacePerformance.is_completion`
- `RacePerformance.is_win`

#### Fixes

- `FinishingPosition.**eq**` with int
- `Outcome.**eq**` with int

#### Refactorings

- replace type checking in `RacePerformance`

## 0.16.0 (2023-09-18)

#### New Features

- `RacePerformance` class
- `Outcome.__repr__` and `__str__`

#### Fixes

- `Outcome.__eq__` handles different types of value
- `Outcome.__init__` typing

## 0.15.0 (2023-09-17)

#### New Features

- add `RaceDesignation` and `RaceLevel` to `RaceConditions`
- add maiden to `RaceDesignation`

#### Fixes

- typing guards for `__eq__` methods
- `__eq__` typing for Liskov subst violation

#### Refactorings

- delete native `ParsingEnum`

#### Others

- import `ParsingEnum` from peak_utility

## 0.14.0 (2023-09-17)

#### New Features

- `Outcome` class

#### Fixes

- `KeyError` on `ParsingEnum` for non string keys

#### Refactorings

- convert `FinishingPosition` enum to class

#### Others

- add `peak-utility`

## 0.13.1 (2023-09-16)

#### Fixes

- `RaceGrade(None)` fails **bool**
- `ValueError` if `Going.primary` and `Going.secondary` match

#### Refactorings

- Going.**repr** and **str**
- HorseAge.**repr** and **str**
- HorseHeight.**repr** and **str**
- Racecourse.**repr** and **str**
- RaceConditions.**repr** and **str**
- RaceDistance.**repr** and **str**
- RaceClass.**repr**
- RaceGrade.**repr**
- RaceLevel.**repr**
- alter Horselength.**repr**

#### Others

- reorganise tests for Horselength.**str**

## 0.13.0 (2023-09-15)

#### New Features

- `RaceLevel` class
- `RaceGrade` class
- `RaceClass` class

#### Fixes

- typing in `Going`

## 0.12.4 (2023-09-15)

#### Fixes

- `Going` cannot be initialised with an invalid string

#### Refactorings

- `Dirt` & `AWGoingDescription` scales align with `Turf`

## 0.12.3 (2023-09-12)

#### Fixes

- add circle to `RacecourseShape` enum
- add assert in `HorseAge` to prevent typing fail

#### Refactorings

- `Racecourse` params can be str or enum

## 0.12.2 (2023-09-12)

#### Fixes

- avoid typing error in `HorseAge`
- add `Stakes` to `RaceDesignation`

#### Others

- test for error on `RaceDistance.init`

## 0.12.1 (2023-09-08)

#### New Features

- `RaceDistance.regex`

#### Refactorings

- remove unneeded conditional in `HorseAge`
- remove unreachable code `HorseAge`

#### Docs

- fix docstrings in `RaceConditions`

#### Others

- complete test coverage for `Gender`

## 0.12.0 (2023-09-06)

#### New Features

- `Racecourse` class
- `Handedness` enum
- `RacecourseStyle` enum
- `RacecourseContour` enum
- `RacecourseShape` enum

#### Fixes

- typing in `RaceConditions.__init__`

#### Refactorings

- swap `Racecourse` for `Surface` in `RaceConditions`

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
