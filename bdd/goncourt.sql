-- phpMyAdmin SQL Dump
-- version 5.2.3
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 10 déc. 2025 à 13:00
-- Version du serveur : 8.4.7
-- Version de PHP : 8.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `goncourt`
--

-- --------------------------------------------------------

--
-- Structure de la table `author`
--

DROP TABLE IF EXISTS `author`;
CREATE TABLE IF NOT EXISTS `author` (
  `Id_Author` int NOT NULL AUTO_INCREMENT,
  `a_first_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `a_last_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `a_biography` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`Id_Author`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `author`
--

INSERT INTO `author` (`Id_Author`, `a_first_name`, `a_last_name`, `a_biography`) VALUES
(1, 'Nathacha', 'APPANAH', NULL),
(2, 'Emmanuel', 'CARRÈRE', 'Emmanuel Carrère est né en 1957. D\'abord journaliste il a publié un essai sur le cinéaste Werner Herzog en 1982 puis L\'Amie du jaguar Bravoure (prix Passion 1984 prix de la Vocation 1985), Le Détroit de Behring essai sur l\'Histoire imaginaire (prix Valery Larbaud et Grand Prix de la science-fiction française 1987),Hors d\'atteinte ? et une biographie du romancier Philip K. Dick : Je suis vivant et vous êtes morts. La Classe de neige prix Femina 1995 a été porté à l\'écran par Claude Miller et L\'Adversaire par Nicole Garcia. En 2003 Emmanuel Carrère réalise un documentaire Retour à Kotelnitch et adapte lui-même en 2004 La Moustache avec Vincent Lindon et Emmanuelle Devos. Il a depuis écrit Un roman russe, D\'autres vies que la mienne, Limonov prix Renaudot 2011, Le Royaume prix littéraire Le Monde, lauréat-palmarès Le Point, Meilleur livre de l\'année, Lire 2014, Il est avantageux d\'avoir où aller et Yoga. En 2020 il a réalisé un nouveau film Ouistreham d\'après le livre de Florence Aubenas avec Juliette Binoche et des actrices non professionnelles. Ses livres sont traduits dans une vingtaine de langues.'),
(3, 'David', 'DENEUFGERMAIN', 'David Deneufgermain est écrivain-médecin. Psychiatre, il a exercé en prison, en hôpital psychiatrique et soigne depuis onze ans les malades à la rue et dans son cabinet. L\'Adieu au visage est son premier roman du réel.'),
(4, 'David', 'DIOP', NULL),
(5, 'Ghislaine', 'DUNANT', 'Ghislaine Dunant a publié trois romans aux éditions Gallimard, dont son premier, très remarqué, L\'Impudeur (1989). Elle a reçu le prix Michel-Dentan (2008) pour Un effondrement et le prix Femina essai pour Charlotte Delbo. La vie retrouvée (2016), tous deux parus chez Grasset.Elle vit à Paris.'),
(6, 'Paul', 'GASNIER', NULL),
(7, 'Yanick', 'LAHENS', NULL),
(8, 'Caroline', 'LAMARCHE', 'Caroline Lamarche vit à Liège. Son œuvre témoigne d’un éclectisme et d’une hardiesse renouvelés de livre en livre. Elle a notamment obtenu le prix Rossel avec Le Jour du Chien (Les Éditions de Minuit) et le Goncourt de la nouvelle pour Nous sommes à la lisière (Gallimard). Elle signe avec Le Bel Obscur son retour au roman.'),
(9, 'Hélène', 'LAURAIN', NULL),
(10, 'Charif', 'MAJDALANI', NULL),
(11, 'Laurent', 'MAUVIGNIER', NULL),
(12, 'Alfred', 'DE MONTESQUIOU', 'Diplômé de Sciences Po, reporter de guerre, lauréat du prix Albert-Londres. Alfred de Montesquiou est réalisateur et écrivain. Son premier roman, L\'Étoile des frontières, est paru en 2021.'),
(13, 'Guillaume', 'POIX', 'Né en 1986, Guillaume Poix a publié plusieurs pièces aux Éditions Théâtrales, dont Soudain Romy Schneider, Un sacre/La vie invisible et Léviathan (matériau). Il est l\'auteur de trois romans aux Éditions Verticales : Les fils conducteurs (prix Wepler-Fondation La Poste, 2017), Là d\'où je viens a disparu (2020) et Star (2023).'),
(14, 'Maria', 'POURCHET', 'Maria Pourchet est écrivaine. Elle est notamment l\'autrice de Rome en un jour (2013), Toutes les femmes sauf une (prix Révélation de la SGDL 2018), Feu (2021) et Western (prix de Flore 2023).'),
(15, 'David', 'THOMAS', 'David Thomas est l’auteur de plusieurs romans et recueils d’instantanés parmi lesquels La Patience des buffles sous la pluie ou Seul entouré de chiens qui mordent (prix de la nouvelle de l’Académie française 2021). Son dernier livre, Partout les autres , a été couronné en 2023 par le prix Goncourt de la nouvelle.');

-- --------------------------------------------------------

--
-- Structure de la table `book`
--

DROP TABLE IF EXISTS `book`;
CREATE TABLE IF NOT EXISTS `book` (
  `Id_Book` int NOT NULL AUTO_INCREMENT,
  `b_title` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `b_summary` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `b_publicationDate` date DEFAULT NULL,
  `b_pagesNb` smallint DEFAULT NULL,
  `b_isbn` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `b_price` decimal(4,2) DEFAULT NULL,
  `Id_Publisher` int NOT NULL,
  `Id_Author` int NOT NULL,
  PRIMARY KEY (`Id_Book`),
  KEY `Id_Publisher` (`Id_Publisher`),
  KEY `Id_Author` (`Id_Author`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `book`
--

INSERT INTO `book` (`Id_Book`, `b_title`, `b_summary`, `b_publicationDate`, `b_pagesNb`, `b_isbn`, `b_price`, `Id_Publisher`, `Id_Author`) VALUES
(1, 'Kolkhose', 'Prix Médicis 2025 - Cette nuit-là, rassemblés tous les trois autour de notre mère, nous avons pour la dernière fois fait kolkhoze .', '2025-08-28', 558, '9782818061985', 24.00, 6, 2),
(2, 'La nuit au coeur', 'Prix Femina 2025 - La nuit au coeur\r\n\r\n« De ces nuits et de ces vies, de ces femmes qui courent, de ces coeurs qui luttent, de ces instants qui sont si accablants qu\'ils ne rentrent pas dans la mesure du temps, il a fallu faire quelque chose. Il y a l\'impossibilité de la vérité entière à chaque page mais la quête désespérée d\'une justesse au plus près de la vie, de la nuit, du coeur, du corps, de l\'esprit.\r\n\r\nDe ces trois femmes, il a fallu commencer par la première, celle qui vient d\'avoir vingt-cinq ans quand elle court et qui est la seule à être encore en vie aujourd\'hui.\r\n\r\nCette femme, c\'est moi. »\r\n\r\nLa nuit au coeur entrelace trois histoires de femmes victimes de la violence de leur compagnon. Sur le fil entre force et humilité, Nathacha Appanah scrute l\'énigme insupportable du féminicide conjugal, quand la nuit noire prend la place de l\'amour.', '2025-08-21', 282, '9782073080028', 21.00, 3, 1),
(3, 'La maison vide', 'Prix Goncourt 2025\r\n\r\nEn 1976, mon père a rouvert la maison qu’il avait reçue de sa mère, restée fermée pendant vingt ans.\r\n\r\nÀ l’intérieur : un piano, une commode au marbre ébréché, une Légion d’honneur, des photographies sur lesquelles un visage a été découpé aux ciseaux.\r\n\r\nUne maison peuplée de récits, où se croisent deux guerres mondiales, la vie rurale de la première moitié du vingtième siècle, mais aussi Marguerite, ma grand-mère, sa mère Marie-Ernestine, la mère de celle-ci, et tous les hommes qui ont gravité autour d’elles.\r\n\r\nToutes et tous ont marqué la maison et ont été progressivement effacés. J’ai tenté de les ramener à la lumière pour comprendre ce qui a pu être leur histoire, et son ombre portée sur la nôtre.', '2025-08-28', 743, '9782707356741', 25.00, 1, 11),
(4, 'Tressaillir', '« J\'ai coupé un lien avec quelque chose d\'aussi étouffant que vital et je ne suis désormais plus branchée sur rien. Ni amour, ni foi, ni médecine. »\r\n\r\nUne femme est partie. Elle a quitté la maison, défait sa vie. Elle pensait découvrir une liberté neuve mais elle éprouve, prostrée dans une chambre d\'hôtel, l\'élémentaire supplice de l\'arrachement. Et si rompre n\'était pas à sa portée ? Si la seule issue au chagrin, c\'était revenir ? Car sans un homme à ses côtés, cette femme a peur. Depuis toujours sur le qui-vive, elle a peur.\r\n\r\nMais au fond, de quoi ?\r\n\r\nDans ce texte du retour aux origines et du retour de la joie, Maria Pourchet entreprend une archéologie de ces terreurs d\'enfant qui hantent les adultes. Elle nous transporte au coeur des forêts du Grand Est sur les traces de drames intimes et collectifs.', '2025-08-20', 324, '9782234097155', 21.90, 4, 14),
(5, 'Un frère', '« Pendant presque quarante ans, il aura été là sans plus vraiment être là. Lui, mais plus lui. Un autre. »\r\n\r\nDavid Thomas raconte le combat de son frère contre cette tyrannie intérieure qu’est la schizophrénie. Sa dureté, sa noirceur, ses ravages. Depuis la mort brutale d’Édouard jusqu’aux années heureuses, il remonte à la source du lien qu’il a eu avec son aîné et grâce auquel il s’est construit. Lors de ce cheminement, il s’interroge : comment écrire cette histoire sans trahir, sans enjoliver ? Écrire pour rejoindre Édouard. Le retrouver.', '2025-08-22', 139, '9782823623376', 19.50, 8, 15),
(6, 'La collision', 'En 2012, en plein centre-ville de Lyon, une femme décède brutalement, percutée par un jeune garçon en moto cross qui fait du rodéo urbain à 80 km/h.\r\n\r\nDix ans plus tard, son fils, qui n\'a cessé d\'être hanté par le drame, est devenu journaliste. Il observe la façon dont ce genre de catastrophe est utilisé quotidiennement pour fracturer la société et dresser une partie de l\'opinion contre l\'autre. Il décide de se replonger dans la complexité de cet accident, et de se lancer sur les traces du motard pour comprendre d\'où il vient, quel a été son parcours et comment un tel événement a été rendu possible.\r\n\r\nEn décortiquant ce drame familial, Paul Gasnier révèle deux destins qui s\'écrivent en parallèle, dans la même ville, et qui s\'ignorent jusqu\'au jour où ils entrent violemment en collision. C\'est aussi l\'histoire de deux familles qui racontent chacune l\'évolution du pays. Un récit en forme d\'enquête littéraire qui explore la force de nos convictions quand le réel les met à mal, et les manquements collectifs qui créent l\'irrémédiable.', '2025-08-21', 160, '9782073101228', 19.00, 3, 6),
(7, 'Le bel obscur', 'Alors qu’elle tente d’élucider le destin d’un ancêtre banni par sa famille, une femme reprend l’histoire de sa propre vie. Des années auparavant, son mari, son premier et grand amour, lui a révélé être homosexuel. Du bouleversement que ce fut dans leur existence comme des péripéties de leur émancipation respective, rien n’est tu. Ce roman lumineux nous offre une leçon de courage, de tolérance, de curiosité aussi. Car jamais cette femme libre n’aura cessé de se réinventer, d’affirmer la puissance de ses rêves contre les conventions sociales, avec une fantaisie et une délicatesse infinies.', '2025-08-22', 229, '9782021603439', 20.00, 2, 8),
(8, 'Où s\'adosse le ciel', 'À la fin du XIXe siècle, Bilal Seck achève un pèlerinage à La Mecque et s\'apprête à rentrer à Saint-Louis du Sénégal. Une épidémie de choléra décime alors la région, mais Bilal en réchappe, sous le regard incrédule d\'un médecin français qui cherche à percer les secrets de son immunité. En pure perte. Déjà, Bilal est ailleurs, porté par une autre histoire, celle qu\'il ne cesse de psalmodier, un mythe immense, demeuré intact en lui, transmis par la grande chaîne de la parole qui le relie à ses ancêtres. Une odyssée qui fut celle du peuple égyptien, alors sous le joug des Ptolémées, conduite par Ounifer, grand prêtre d\'Osiris qui caressait le rêve de rendre leur liberté aux siens, les menant vers l\'ouest à travers les déserts, jusqu\'à une terre promise, un bel horizon, là où s\'adosse le ciel...\r\nCe chemin, Bilal l\'emprunte à son tour, vers son pays natal, en passant par Djenné, la cité rouge, où vint buter un temps le voyage d\'Ounifer et de son peuple.\r\n\r\nDe l\'Égypte ancienne au Sénégal, David Diop signe un roman magistral sur un homme parti à la reconquête de ses origines et des sources immémoriales de sa parole.', '2025-08-14', 363, '9782260057307', 22.50, 9, 4),
(9, 'L\' Adieu au visage', 'Un roman en apnée sur la pandémie. Ce qu\'elle a fait aux vivants et aux morts, à notre humanité.\r\n\r\nMars 2020. La France se confine. Dans tous les hôpitaux du pays, il faut prendre des décisions et agir vite. En première ligne, un psychiatre partage son temps entre son équipe mobile qui maraude dans une ville fantôme à la recherche de marginaux à protéger, et les unités covid où les malades meurent seuls, privés de tout rite. Entre obéissance à la loi et refus de l\'horreur, que ce soit à l\'hôpital ou dehors, chacun à son niveau cherche des solutions et improvise. L\'Adieu au visage est l\'écriture d\'une résistance fragile et d\'une lutte pour prendre soin de l\'autre.\r\n\r\n« Au commencement, on ne lave plus les corps, on ne les coiffe plus, on ne les habille plus, on ne les présente plus - d\'accompagner les morts, il n\'est plus question. »', '2025-12-20', 261, '9782381340647', 21.10, 10, 3),
(10, 'Passagères de nuit', 'Dans ce nouveau roman, comme arraché au chaos de son quotidien à Port-au-Prince, Yanick Lahens rend un hommage d’espoir et de résistance à la lignée des femmes dont elle est issue.\r\nLa première d’entre elles, Élizabeth Dubreuil, naît vers 1820 à La Nouvelle-Orléans. Sa grand-mère, arrivée d’Haïti au début du siècle dans le sillage du maître de la plantation qui avait fini par l’affranchir, n’a plus jamais voulu dépendre d’un homme. Inspirée par ce puissant exemple, la jeune Élisabeth se rebelle à son tour contre le désir prédateur d’un ami de son père. Elle doit fuir la ville, devenant à son tour une « passagère de nuit » sur un bateau à destination de Port-au-Prince. Ce qui adviendra d’elle, nous l’apprendrons quand son existence croisera celle de Régina, autre grande figure de ce roman des origines.\r\nNée pauvre parmi les pauvres dans un hameau du sud de l’île d’Haïti, Régina elle aussi a forcé le destin : rien ne la déterminait à devenir la maîtresse d’un des généraux arrivé en libérateur à Port-au-Prince en 1867. C’est à « mon général, mon amant, mon homme » qu’elle adresse le monologue amoureux dans lequel elle évoque sa trajectoire d’émancipation : la cruauté mesquine des maîtres qu’elle a fuis trouve son contrepoint dans les mains tendues par ces femmes qui lui ont appris à opposer aux coups du sort une ténacité silencieuse.\r\nCette ténacité silencieuse, Élizabeth et Régina l’ont reçue en partage de leurs lointaines ascendantes, ces « passagères de nuit » des bateaux négriers, dont Yanick Lahens évoque ici l’effroyable réalité, de même qu’elle nous plonge – et ce n’est pas la moindre qualité de ce très grand livre – dans les convulsions de l’histoire haïtienne.\r\nLorsque les deux héroïnes se rencontreront, dans une scène d’une rare qualité d’émotion, nous, lectrices et lecteurs, comprendrons que l’histoire ne s’écrit pas seulement avec les vainqueurs, mais dans la beauté des gestes, des regards et des mystères tus, qui à bas bruit montrent le chemin d’une résistance forçant l’admiration.\r\n\r\n', '2025-08-28', 223, '9782848055701', 20.00, 11, 7),
(11, 'Le nom des rois', '« Et d\'un seul coup, le monde qui servait de décor à tout cela s\'écroula. J\'en avais été un témoin distrait, mais le bruit qu\'il provoqua en s\'effondrant me fit lever la tête et ce que je vis alors n\'était plus qu\'un univers de violence et de mort. C\'est de celui-là que je suis devenu contemporain. J\'avais été, durant des années, dispensé d\'intérêt pour ce qui se passait autour de moi par ma passion des atlas, par les royautés anciennes et inutiles et par les terres lointaines et isolées, les berceaux de vieux empires oubliés.\r\n\r\nDésormais, l\'histoire se faisait sous mes yeux et je la trouvais moche, roturière et vulgaire. »\r\n\r\nDans ce récit de passage à l\'âge adulte porté par une écriture ample et élégante, Charif Majdalani raconte la disparition d\'un pays et explore ce qui subsiste de l\'enfance lorsqu\'elle capitule devant les fracas du monde.', '2025-08-20', 214, '9782234097278', 20.00, 4, 10),
(12, 'Un amour infini', 'Première sélection duPrix Goncourt 2025.\r\n\r\nPremière sélection du prix Médicis 2025.\r\n\r\nUne parenthèse d\'une grâce absolue, qu\'on voudrait ne jamais refermer. Lire - Magazine littéraire\r\n\r\nElle est descendue en retard, elle voulait encore fumer une cigarette, fumer seule, une fois de plus. Pour sentir le temps qui passe, ne plus savoir qui elle est, ni ce qu\'on peut vouloir d\'elle.\r\n\r\nCe roman installe le lecteur au coeur d\'une rencontre de trois jours sur l\'île de Ténérife, en juin 1964, prévue mais bouleversée par un événement tragique, entre un astrophysicien d\'origine hongroise qui a dû fuir l\'Europe et s\'exiler aux États-Unis et une mère de famille française.\r\n\r\nAlors que rien ne devrait les rapprocher, leurs conversations sur leurs passés distincts et l\'exploration de l\'île vont les ouvrir profondément l\'un à l\'autre. Le ciel, l\'univers, l\'histoire de la Terre... Les sujets de l\'astrophysicien rejoignent la sensibilité de celle qui a observé le mystère de la toute petite enfance et a toujours eu une approche sensitive des êtres. Leur désir réciproque va s\'accompagner de la puissance des éléments qui les entourent.\r\n\r\n1964. Sur l\'île de Tenerife. Une femme et un homme que rien ne destinait à se rencontrer, et, pourtant, durant 3 jours, en cette géographie volcanique et insulaire, naîtra l\'une des plus belles rencontres amoureuses écrites ces dernières années...Roman sensible subtile et sensuel, où le paysage cosmique, absolu de l\'île de Tenerife et la rencontre entre Louise et Nathan confluent si intimement que l\'impression laissée par cette histoire à l\'écriture aussi délicate que tellurique perdure infiniment.\r\n\r\nKarine Henry - Librairie Comme Un roman', '2025-08-20', 170, '	 9782226498687', 19.90, 5, 5),
(13, 'Tambora', 'Une mère nous parle de ses deux filles, qu’elle voit amples comme des villes en expansion. La première est déjà là quand le récit commence, la seconde naîtra bientôt, après la perte d’un autre enfant lors d’une fausse couche. Ici, la temporalité de la maternité domine : celle de grossesses compliquées, d’hôpitaux et de services des urgences, la temporalité d’un corps qui produit, parfois sans qu’on le veuille, la temporalité de la naissance, celle des soins, ou des désirs trop souvent empêchés. Mais d’autres réalités existent aussi, se faufilent et tentent de prendre leur place : un manuscrit qui intéresse un éditeur, des confinements, qui ne changent pas grand-chose lorsqu’on doit rester alitée, la catastrophe environnementale qui se déploie, gigantesque, et fait songer à la fin du monde que l’humanité a cru vivre en 1815 quand l’éruption du volcan Tambora plongea une partie de la Terre dans le froid et l’obscurité. Hélène Laurain écrit avec cela, et écrit tout cela, avec crudité parfois. Son livre conjugue récit, réflexions et poésie, et nous emmène à la rencontre d’un monde incertain.', '2025-08-28', 192, '9782378562588', 18.50, 7, 9),
(14, 'Perpétuité', '18h45. Une maison d\'arrêt du sud de la France. Pierre, Houda, Laurent, Maëva et d\'autres surveillants prennent leur service de nuit. Captifs d\'une routine qui menace à chaque instant de déraper, ces agents de la pénitentiaire vont traverser ensemble une série d\'incidents plus éprouvants qu\'à l\'ordinaire.\r\n\r\nEn regardant celles et ceux qui regardent, Guillaume Poix plonge dans le quotidien d\'un métier méconnu, sinon méprisé, et interroge le sens d\'une institution au bord du gouffre.', '2025-08-21', 331, '9782073105455', 22.00, 12, 13),
(15, 'Le crépuscule des hommes', 'PRIX RENAUDOT ESSAI 2025\r\nSélection Prix Goncourt des lycéens\r\nSélection Prix Goncourt des détenus\r\nNuremberg, 1945 : un procès fait l\'Histoire, eux la vivent. Un roman vrai, qui saisit les sursauts de l\'Histoire en marche.\r\nChacun connaît les images du procès de Nuremberg, où Göring et vingt autres nazis sont jugés à partir de novembre 1945. Mais que se passe-t-il hors de la salle d\'audience ?\r\nIls sont là : Joseph Kessel, Elsa Triolet, Martha Gellhorn ou encore John Dos Passos, venus assister à ces dix mois où doit oeuvrer la justice. Des dortoirs de l\'étrange château Faber-Castell, qui loge la presse internationale, aux box des accusés, tous partagent la frénésie des reportages, les frictions entre alliés occidentaux et soviétiques, l\'effroi que suscite le récit inédit des déportés.\r\nAvec autant de précision historique que de tension romanesque, Alfred de Montesquiou ressuscite des hommes et des femmes de l\'ombre, témoins du procès le plus retentissant du XXe siècle.', '2025-08-28', 382, '9782221267660', 22.00, 13, 12);

-- --------------------------------------------------------

--
-- Structure de la table `character_table`
--

DROP TABLE IF EXISTS `character_table`;
CREATE TABLE IF NOT EXISTS `character_table` (
  `Id_Character` int NOT NULL AUTO_INCREMENT,
  `c_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `Id_Book` int NOT NULL,
  PRIMARY KEY (`Id_Character`),
  KEY `Id_Book` (`Id_Book`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `character_table`
--

INSERT INTO `character_table` (`Id_Character`, `c_name`, `Id_Book`) VALUES
(1, 'La mère ', 1),
(2, 'Femme1', 2),
(3, 'Femme2', 2),
(4, 'Autrice', 2),
(5, 'Le père', 3),
(6, 'Marguerite', 3),
(7, 'Marie-Ernestine', 3),
(8, 'Maria', 4),
(9, 'Frère auteur', 5),
(10, 'Jeune garçon', 6),
(11, 'Le fils', 6),
(12, 'Une épouse', 7),
(13, 'Le mari', 7),
(14, 'Bilal Seck', 8),
(15, 'Ounifer', 8),
(16, 'Elizabeth Dubreuil', 10),
(17, 'Regina', 10),
(18, 'La grand-mère', 10),
(19, 'Une femme', 12),
(20, 'Un homme', 12),
(21, 'Une mère', 13),
(22, 'Fille1', 13),
(23, 'Fille2', 13),
(24, 'Pierre', 14),
(25, 'Houda', 14),
(26, 'Laurent', 14),
(27, 'Maëva', 14),
(28, 'Göring', 15),
(29, 'Joseph Kessel', 15),
(30, 'Elsa Triolet', 15),
(31, 'Martha Gellhorn', 15),
(32, 'John Dos Passos', 15);

-- --------------------------------------------------------

--
-- Structure de la table `jurymember`
--

DROP TABLE IF EXISTS `jurymember`;
CREATE TABLE IF NOT EXISTS `jurymember` (
  `Id_JuryMember` int NOT NULL AUTO_INCREMENT,
  `j_first_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `j_last_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `j_connection_id` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `j_password` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `j_role` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id_JuryMember`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `jurymember`
--

INSERT INTO `jurymember` (`Id_JuryMember`, `j_first_name`, `j_last_name`, `j_connection_id`, `j_password`, `j_role`) VALUES
(1, 'Didier', 'DECOIN', NULL, NULL, 'Membre'),
(2, 'Françoise', 'CHANDERNAGOR', NULL, NULL, 'Membre'),
(3, 'Tahar', 'BEN JELLOUN', NULL, NULL, 'Membre'),
(4, 'Paule', 'CONSTANT', NULL, NULL, 'Membre'),
(5, 'Philippe', 'CLAUDEL', NULL, NULL, 'Président'),
(6, 'Pierre', 'ASSOULINE', NULL, NULL, 'Membre'),
(7, 'Eric-Emmanuel', 'SCHMITT', NULL, NULL, 'Membre'),
(8, 'Camille', 'LAURENS', NULL, NULL, 'Membre'),
(9, 'Pascal', 'BRUCKNER', NULL, NULL, 'Membre'),
(10, 'Christine', 'ANGOT', NULL, NULL, 'Membre');

-- --------------------------------------------------------

--
-- Structure de la table `possess`
--

DROP TABLE IF EXISTS `possess`;
CREATE TABLE IF NOT EXISTS `possess` (
  `Id_Book` int NOT NULL,
  `Id_Selection` int NOT NULL,
  PRIMARY KEY (`Id_Book`,`Id_Selection`),
  KEY `Id_Selection` (`Id_Selection`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `possess`
--

INSERT INTO `possess` (`Id_Book`, `Id_Selection`) VALUES
(1, 1),
(2, 1),
(3, 1),
(4, 1),
(5, 1),
(6, 1),
(7, 1),
(8, 1),
(9, 1),
(10, 1),
(11, 1),
(12, 1),
(13, 1),
(14, 1),
(15, 1);

-- --------------------------------------------------------

--
-- Structure de la table `publisher`
--

DROP TABLE IF EXISTS `publisher`;
CREATE TABLE IF NOT EXISTS `publisher` (
  `Id_Publisher` int NOT NULL AUTO_INCREMENT,
  `p_name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `p_address` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Id_Publisher`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `publisher`
--

INSERT INTO `publisher` (`Id_Publisher`, `p_name`, `p_address`) VALUES
(1, 'Éditions de Minuit', '7 rue Bernard-Palissy, 75006 Paris'),
(2, 'Seuil', '27 rue Jacob, 75006 Paris'),
(3, 'Gallimard', '5 rue Sébastien-Bottin, 75328 Paris Cedex 07'),
(4, 'Stock', '120 boulevard Saint-Germain, 75006 Paris'),
(5, 'Albin Michel', '22 rue Huyghens, 75014 Paris'),
(6, 'POL (Paul Otchakovsky-Laurens)', '33 rue Saint-André-des-Arts, 75006 Paris'),
(7, 'Verdier', 'Le Chambon, 84110 Lagrasse'),
(8, 'Éditions de l’Olivier', '96 boulevard Saint-Germain, 75006 Paris'),
(9, 'Julliard', '22 rue du Pont-Neuf 75001 Paris'),
(10, 'Edition Marchialy', '12 rue Jean-Jacques Rousseau, 93100 Montreuil'),
(11, 'Sabine Wespieser', '13 Rue de l\'abbé grégoire, 75006 Paris'),
(12, 'Verticales', '93, rue Vieille-du-Temple, 75003 Paris'),
(13, 'R.Laffont', '92 Avenue de France, 75013 Paris');

-- --------------------------------------------------------

--
-- Structure de la table `selection`
--

DROP TABLE IF EXISTS `selection`;
CREATE TABLE IF NOT EXISTS `selection` (
  `Id_Selection` int NOT NULL AUTO_INCREMENT,
  `s_date` date DEFAULT NULL,
  `s_number` smallint DEFAULT NULL,
  PRIMARY KEY (`Id_Selection`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Déchargement des données de la table `selection`
--

INSERT INTO `selection` (`Id_Selection`, `s_date`, `s_number`) VALUES
(1, '2025-09-03', 1);

-- --------------------------------------------------------

--
-- Structure de la table `vote`
--

DROP TABLE IF EXISTS `vote`;
CREATE TABLE IF NOT EXISTS `vote` (
  `Id_Vote` int NOT NULL AUTO_INCREMENT,
  `Id_Book` int NOT NULL,
  `Id_JuryMember` int NOT NULL,
  PRIMARY KEY (`Id_Vote`),
  KEY `Id_Book` (`Id_Book`),
  KEY `Id_JuryMember` (`Id_JuryMember`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `book`
--
ALTER TABLE `book`
  ADD CONSTRAINT `book_ibfk_1` FOREIGN KEY (`Id_Publisher`) REFERENCES `publisher` (`Id_Publisher`),
  ADD CONSTRAINT `book_ibfk_2` FOREIGN KEY (`Id_Author`) REFERENCES `author` (`Id_Author`);

--
-- Contraintes pour la table `character_table`
--
ALTER TABLE `character_table`
  ADD CONSTRAINT `character_table_ibfk_1` FOREIGN KEY (`Id_Book`) REFERENCES `book` (`Id_Book`);

--
-- Contraintes pour la table `possess`
--
ALTER TABLE `possess`
  ADD CONSTRAINT `possess_ibfk_1` FOREIGN KEY (`Id_Book`) REFERENCES `book` (`Id_Book`),
  ADD CONSTRAINT `possess_ibfk_2` FOREIGN KEY (`Id_Selection`) REFERENCES `selection` (`Id_Selection`);

--
-- Contraintes pour la table `vote`
--
ALTER TABLE `vote`
  ADD CONSTRAINT `vote_ibfk_1` FOREIGN KEY (`Id_Book`) REFERENCES `book` (`Id_Book`),
  ADD CONSTRAINT `vote_ibfk_2` FOREIGN KEY (`Id_JuryMember`) REFERENCES `jurymember` (`Id_JuryMember`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
