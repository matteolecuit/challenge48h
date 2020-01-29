function getHistory(req, res) {
    const response = [
        {"index": 1, 
        "timestamp": "2020-01-28 09:06:43.544337",
        "data": " Guy de Maupassant Bel-Ami       BeQ \n   Guy de Maupassant Bel-Ami  roman            La Biblioth\u00e8que \u00e9lectronique du Qu\u00e9bec Collection \u00c0 tous les vents Volume 510 : version 1.01  2\n Du m\u00eame auteur, \u00e0 la Biblioth\u00e8que  Mademoiselle Fifi Contes de la b\u00e9casse Pierre et Jean Sur l\u2122eau La maison Tellier La petite Roque Une vie Fort comme la mort Clair de lune Miss Harriet La main gauche Yvette L\u2122inutile beaut\u00e9 Monsieur Parent Le Horla Les soeurs Rondoli Le docteur H\u00e9raclius Gloss et autres contes Les dimanches d\u2122un bourgeois de Paris Le rosier de Madame Husson Contes du jour et de la nuit La vie errante Notre coeur  3\n      Bel-Ami   \u00c9dition de r\u00e9f\u00e9rence : \u00c9ditions Rencontre, Lausanne. Texte \u00e9tabli et pr\u00e9sent\u00e9 par Gilbert Sigaux.  4\n     Premi\u00e8re partie  5\n", 
        "contributor_id": "insert your contributor_id here (40bit)", 
        "previous_hash": "63b74860ef72735b5e3a01a5aff884952484da32c37c0c6c351d8ecaabd18d3d", 
        "nonce": 14, 
        "difficulty": 1, 
        "hash": "b10b22134bc01558c79a936b9e5873a881bd9dbf294a242de4430739a52dba3c"},
        {"index": 2, 
        "timestamp": "2019-01-25 09:06:43.544337",
        "data": " Guy de Maupassant Bel-Ami       BeQ \n   Guy de Maupassant Bel-Ami  roman            La Biblioth\u00e8que \u00e9lectronique du Qu\u00e9bec Collection \u00c0 tous les vents Volume 510 : version 1.01  2\n Du m\u00eame auteur, \u00e0 la Biblioth\u00e8que  Mademoiselle Fifi Contes de la b\u00e9casse Pierre et Jean Sur l\u2122eau La maison Tellier La petite Roque Une vie Fort comme la mort Clair de lune Miss Harriet La main gauche Yvette L\u2122inutile beaut\u00e9 Monsieur Parent Le Horla Les soeurs Rondoli Le docteur H\u00e9raclius Gloss et autres contes Les dimanches d\u2122un bourgeois de Paris Le rosier de Madame Husson Contes du jour et de la nuit La vie errante Notre coeur  3\n      Bel-Ami   \u00c9dition de r\u00e9f\u00e9rence : \u00c9ditions Rencontre, Lausanne. Texte \u00e9tabli et pr\u00e9sent\u00e9 par Gilbert Sigaux.  4\n     Premi\u00e8re partie  5\n", 
        "contributor_id": "insert your contributor_id here (40bit)", 
        "previous_hash": "73b74860ef72735b5e3a01a5aff884952484da32c37c0c6c351d8ecaabd18d3d", 
        "nonce": 11, 
        "difficulty": 2, 
        "hash": "a10b22134bc01558c79a936b9e5873a881bd9dbf294a242de4430739a52dba3c"},

    ]
        
    res.send(response)
}
function getById(req, res) {
    const { id } = req.params;
    if (!id) {
        res.status(400).send();
    } else {
        Block.findById(id).thenb(block => {
            if (!block) {
                res.status(404).send();
            } else {
                res.send(block);
            }
        }).catch(err => res.status(500).send(err));
    }
}
const postBlock = (req, res) => {
    const newBlock=
        new Block({
            index: req.body.index,
            timestamp: req.body.timestamp,
            data: req.body.data,
            contributor_id: req.body.contributor_id,
            previous_hash: req.body.previous_hash,
            nonce: req.body.nonce,
            hash: req.body.hash
        });
    newBlock.save().then(block => res.json(block)).catch(err => res.status(500).send(err));
}
function post(req, res) {
    res.status(200).send();
}

module.exports = {
    getById,
    post,
    postBlock,
    getHistory
}