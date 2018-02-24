use test
db.stuff.drop()

for (let i = 0; i < 1000; i++){
    let doc = {
        a: Math.floor((Math.random() * 10000) + 1),
        b: Math.floor((Math.random() * 10000) + 1),
        c: Math.floor((Math.random() * 10000) + 1),
    };
    db.stuff.insert(doc);
}