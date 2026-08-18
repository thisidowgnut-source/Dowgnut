export type Flavor = { id: string; name: string; price: number; tag: string; accent: string; description: string };
export const flavors: Flavor[] = [
  { id:'classic', name:'Classic Glaze', price:4.5, tag:'OG', accent:'#FFD34E', description:'Soft yeast doughnut with a clean glossy glaze.' },
  { id:'drizzle', name:'Pink Drizzle', price:5.5, tag:'FLAVA', accent:'#FF6FAE', description:'Vanilla glaze with strawberry drizzle and a bright finish.' },
  { id:'sprinkled', name:'Sprinkled Pop', price:5.9, tag:'POPULAR', accent:'#67D4B4', description:'Creamy glaze, rainbow sprinkles and maximum good vibes.' },
  { id:'choco', name:'Choco Crush', price:6.2, tag:'NEW', accent:'#8A5A44', description:'Deep chocolate glaze with a fudgy bite.' },
];
