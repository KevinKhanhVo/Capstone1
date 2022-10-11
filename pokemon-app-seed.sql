-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/96UNmb
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

SET XACT_ABORT ON

BEGIN TRANSACTION QUICKDBD

CREATE TABLE [Trainer] (
    [TrainerID] int  NOT NULL ,
    [Name] text  NOT NULL ,
    [Gender] text  NOT NULL ,
    CONSTRAINT [PK_Trainer] PRIMARY KEY CLUSTERED (
        [TrainerID] ASC
    )
)

CREATE TABLE [Pokemon] (
    [PokemonID] int  NOT NULL ,
    [Name] text  NOT NULL ,
    [Generation] text  NOT NULL ,
    [Type] int  NOT NULL ,
    [Location] int  NOT NULL ,
    [TrainerID] int  NOT NULL ,
    CONSTRAINT [PK_Pokemon] PRIMARY KEY CLUSTERED (
        [PokemonID] ASC
    )
)

CREATE TABLE [Moveset] (
    [MovesetID] int  NOT NULL ,
    [MoveID] int  NOT NULL ,
    [PokemonID] int  NOT NULL ,
    CONSTRAINT [PK_Moveset] PRIMARY KEY CLUSTERED (
        [MovesetID] ASC
    )
)

CREATE TABLE [Move] (
    [MoveID] int  NOT NULL ,
    [Name] text  NOT NULL ,
    [Type] text  NOT NULL ,
    CONSTRAINT [PK_Move] PRIMARY KEY CLUSTERED (
        [MoveID] ASC
    )
)

CREATE TABLE [PokemonType] (
    [PokemonTypeID] int  NOT NULL ,
    [Name] text  NOT NULL ,
    CONSTRAINT [PK_PokemonType] PRIMARY KEY CLUSTERED (
        [PokemonTypeID] ASC
    )
)

CREATE TABLE [Location] (
    [LocationID] int  NOT NULL ,
    [Name] text  NOT NULL ,
    [Region] text  NOT NULL ,
    CONSTRAINT [PK_Location] PRIMARY KEY CLUSTERED (
        [LocationID] ASC
    )
)

CREATE TABLE [Evolution] (
    [EvolutionID] int  NOT NULL ,
    [PokemonID] int  NOT NULL ,
    [EvolutionChainID] int  NOT NULL ,
    CONSTRAINT [PK_Evolution] PRIMARY KEY CLUSTERED (
        [EvolutionID] ASC
    )
)

CREATE TABLE [EvolutionChain] (
    [EvolutionChainID] int  NOT NULL ,
    [Is_baby] boolean  NOT NULL ,
    [Evolves_to] text  NOT NULL ,
    [Trigger] text  NOT NULL ,
    CONSTRAINT [PK_EvolutionChain] PRIMARY KEY CLUSTERED (
        [EvolutionChainID] ASC
    )
)

ALTER TABLE [Pokemon] WITH CHECK ADD CONSTRAINT [FK_Pokemon_Type] FOREIGN KEY([Type])
REFERENCES [PokemonType] ([PokemonTypeID])

ALTER TABLE [Pokemon] CHECK CONSTRAINT [FK_Pokemon_Type]

ALTER TABLE [Pokemon] WITH CHECK ADD CONSTRAINT [FK_Pokemon_Location] FOREIGN KEY([Location])
REFERENCES [Location] ([LocationID])

ALTER TABLE [Pokemon] CHECK CONSTRAINT [FK_Pokemon_Location]

ALTER TABLE [Pokemon] WITH CHECK ADD CONSTRAINT [FK_Pokemon_TrainerID] FOREIGN KEY([TrainerID])
REFERENCES [Trainer] ([TrainerID])

ALTER TABLE [Pokemon] CHECK CONSTRAINT [FK_Pokemon_TrainerID]

ALTER TABLE [Moveset] WITH CHECK ADD CONSTRAINT [FK_Moveset_MoveID] FOREIGN KEY([MoveID])
REFERENCES [Move] ([MoveID])

ALTER TABLE [Moveset] CHECK CONSTRAINT [FK_Moveset_MoveID]

ALTER TABLE [Moveset] WITH CHECK ADD CONSTRAINT [FK_Moveset_PokemonID] FOREIGN KEY([PokemonID])
REFERENCES [Pokemon] ([PokemonID])

ALTER TABLE [Moveset] CHECK CONSTRAINT [FK_Moveset_PokemonID]

ALTER TABLE [Evolution] WITH CHECK ADD CONSTRAINT [FK_Evolution_PokemonID] FOREIGN KEY([PokemonID])
REFERENCES [Pokemon] ([PokemonID])

ALTER TABLE [Evolution] CHECK CONSTRAINT [FK_Evolution_PokemonID]

ALTER TABLE [Evolution] WITH CHECK ADD CONSTRAINT [FK_Evolution_EvolutionChainID] FOREIGN KEY([EvolutionChainID])
REFERENCES [EvolutionChain] ([EvolutionChainID])

ALTER TABLE [Evolution] CHECK CONSTRAINT [FK_Evolution_EvolutionChainID]

COMMIT TRANSACTION QUICKDBD