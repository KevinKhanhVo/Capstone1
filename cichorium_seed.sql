--
-- PostgreSQL database dump
--

-- Dumped from database version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.11 (Ubuntu 12.11-0ubuntu0.20.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: location; Type: TABLE; Schema: public; Owner: kevin
--

CREATE TABLE public.location (
    id integer NOT NULL,
    name text NOT NULL,
    pokemon_id integer
);


ALTER TABLE public.location OWNER TO kevin;

--
-- Name: location_id_seq; Type: SEQUENCE; Schema: public; Owner: kevin
--

CREATE SEQUENCE public.location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_id_seq OWNER TO kevin;

--
-- Name: location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kevin
--

ALTER SEQUENCE public.location_id_seq OWNED BY public.location.id;


--
-- Name: move; Type: TABLE; Schema: public; Owner: kevin
--

CREATE TABLE public.move (
    id integer NOT NULL,
    name text NOT NULL,
    pokemon_id integer
);


ALTER TABLE public.move OWNER TO kevin;

--
-- Name: move_id_seq; Type: SEQUENCE; Schema: public; Owner: kevin
--

CREATE SEQUENCE public.move_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.move_id_seq OWNER TO kevin;

--
-- Name: move_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kevin
--

ALTER SEQUENCE public.move_id_seq OWNED BY public.move.id;


--
-- Name: pokemon; Type: TABLE; Schema: public; Owner: kevin
--

CREATE TABLE public.pokemon (
    id integer NOT NULL,
    name text NOT NULL,
    trainer_id integer,
    image_url text
);


ALTER TABLE public.pokemon OWNER TO kevin;

--
-- Name: pokemon_id_seq; Type: SEQUENCE; Schema: public; Owner: kevin
--

CREATE SEQUENCE public.pokemon_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pokemon_id_seq OWNER TO kevin;

--
-- Name: pokemon_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kevin
--

ALTER SEQUENCE public.pokemon_id_seq OWNED BY public.pokemon.id;


--
-- Name: pokemontype; Type: TABLE; Schema: public; Owner: kevin
--

CREATE TABLE public.pokemontype (
    id integer NOT NULL,
    name text NOT NULL,
    pokemon_id integer
);


ALTER TABLE public.pokemontype OWNER TO kevin;

--
-- Name: pokemontype_id_seq; Type: SEQUENCE; Schema: public; Owner: kevin
--

CREATE SEQUENCE public.pokemontype_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.pokemontype_id_seq OWNER TO kevin;

--
-- Name: pokemontype_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kevin
--

ALTER SEQUENCE public.pokemontype_id_seq OWNED BY public.pokemontype.id;


--
-- Name: trainer; Type: TABLE; Schema: public; Owner: kevin
--

CREATE TABLE public.trainer (
    id integer NOT NULL,
    trainer_name text NOT NULL,
    username text NOT NULL,
    password text NOT NULL,
    image_url text
);


ALTER TABLE public.trainer OWNER TO kevin;

--
-- Name: trainer_id_seq; Type: SEQUENCE; Schema: public; Owner: kevin
--

CREATE SEQUENCE public.trainer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trainer_id_seq OWNER TO kevin;

--
-- Name: trainer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: kevin
--

ALTER SEQUENCE public.trainer_id_seq OWNED BY public.trainer.id;


--
-- Name: location id; Type: DEFAULT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.location ALTER COLUMN id SET DEFAULT nextval('public.location_id_seq'::regclass);


--
-- Name: move id; Type: DEFAULT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.move ALTER COLUMN id SET DEFAULT nextval('public.move_id_seq'::regclass);


--
-- Name: pokemon id; Type: DEFAULT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemon ALTER COLUMN id SET DEFAULT nextval('public.pokemon_id_seq'::regclass);


--
-- Name: pokemontype id; Type: DEFAULT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemontype ALTER COLUMN id SET DEFAULT nextval('public.pokemontype_id_seq'::regclass);


--
-- Name: trainer id; Type: DEFAULT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.trainer ALTER COLUMN id SET DEFAULT nextval('public.trainer_id_seq'::regclass);


--
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kevin
--

SELECT pg_catalog.setval('public.location_id_seq', 223, true);


--
-- Name: move_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kevin
--

SELECT pg_catalog.setval('public.move_id_seq', 297, true);


--
-- Name: pokemon_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kevin
--

SELECT pg_catalog.setval('public.pokemon_id_seq', 71, true);


--
-- Name: pokemontype_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kevin
--

SELECT pg_catalog.setval('public.pokemontype_id_seq', 93, true);


--
-- Name: trainer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: kevin
--

SELECT pg_catalog.setval('public.trainer_id_seq', 17, true);


--
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (id);


--
-- Name: move move_pkey; Type: CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.move
    ADD CONSTRAINT move_pkey PRIMARY KEY (id);


--
-- Name: pokemon pokemon_pkey; Type: CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemon
    ADD CONSTRAINT pokemon_pkey PRIMARY KEY (id);


--
-- Name: pokemontype pokemontype_pkey; Type: CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemontype
    ADD CONSTRAINT pokemontype_pkey PRIMARY KEY (id);


--
-- Name: trainer trainer_pkey; Type: CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.trainer
    ADD CONSTRAINT trainer_pkey PRIMARY KEY (id);


--
-- Name: location location_pokemon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pokemon_id_fkey FOREIGN KEY (pokemon_id) REFERENCES public.pokemon(id);


--
-- Name: move move_pokemon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.move
    ADD CONSTRAINT move_pokemon_id_fkey FOREIGN KEY (pokemon_id) REFERENCES public.pokemon(id);


--
-- Name: pokemon pokemon_trainer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemon
    ADD CONSTRAINT pokemon_trainer_id_fkey FOREIGN KEY (trainer_id) REFERENCES public.trainer(id);


--
-- Name: pokemontype pokemontype_pokemon_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: kevin
--

ALTER TABLE ONLY public.pokemontype
    ADD CONSTRAINT pokemontype_pokemon_id_fkey FOREIGN KEY (pokemon_id) REFERENCES public.pokemon(id);


--
-- PostgreSQL database dump complete
--

