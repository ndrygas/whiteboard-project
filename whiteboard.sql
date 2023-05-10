--
-- PostgreSQL database dump
--

-- Dumped from database version 14.7 (Homebrew)
-- Dumped by pg_dump version 14.7 (Homebrew)

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
-- Name: notes; Type: TABLE; Schema: public; Owner: Cryotics
--

CREATE TABLE public.notes (
    note_id integer NOT NULL,
    user_id integer,
    title character varying(50),
    body text,
    favorite boolean NOT NULL,
    shared boolean NOT NULL
);


ALTER TABLE public.notes OWNER TO "Cryotics";

--
-- Name: notes_note_id_seq; Type: SEQUENCE; Schema: public; Owner: Cryotics
--

CREATE SEQUENCE public.notes_note_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.notes_note_id_seq OWNER TO "Cryotics";

--
-- Name: notes_note_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Cryotics
--

ALTER SEQUENCE public.notes_note_id_seq OWNED BY public.notes.note_id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: Cryotics
--

CREATE TABLE public.users (
    user_id integer NOT NULL,
    username character varying(30) NOT NULL,
    password character varying(30) NOT NULL
);


ALTER TABLE public.users OWNER TO "Cryotics";

--
-- Name: users_user_id_seq; Type: SEQUENCE; Schema: public; Owner: Cryotics
--

CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_user_id_seq OWNER TO "Cryotics";

--
-- Name: users_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: Cryotics
--

ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;


--
-- Name: notes note_id; Type: DEFAULT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.notes ALTER COLUMN note_id SET DEFAULT nextval('public.notes_note_id_seq'::regclass);


--
-- Name: users user_id; Type: DEFAULT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);


--
-- Data for Name: notes; Type: TABLE DATA; Schema: public; Owner: Cryotics
--

COPY public.notes (note_id, user_id, title, body, favorite, shared) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: Cryotics
--

COPY public.users (user_id, username, password) FROM stdin;
1	nico	pico
2	wico	lico
\.


--
-- Name: notes_note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Cryotics
--

SELECT pg_catalog.setval('public.notes_note_id_seq', 1, false);


--
-- Name: users_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: Cryotics
--

SELECT pg_catalog.setval('public.users_user_id_seq', 2, true);


--
-- Name: notes notes_pkey; Type: CONSTRAINT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_pkey PRIMARY KEY (note_id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: notes notes_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: Cryotics
--

ALTER TABLE ONLY public.notes
    ADD CONSTRAINT notes_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(user_id);


--
-- PostgreSQL database dump complete
--

