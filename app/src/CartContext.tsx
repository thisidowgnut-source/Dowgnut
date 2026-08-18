import { createContext, useContext, useMemo, useState } from 'react';
import { Flavor } from './flavors';
type Line = Flavor & { qty:number };
type Ctx = { items:Line[]; add:(f:Flavor)=>void; remove:(id:string)=>void; total:number; count:number };
const CartContext=createContext<Ctx|null>(null);
export function CartProvider({children}:{children:React.ReactNode}){const [items,setItems]=useState<Line[]>([]);const add=(f:Flavor)=>setItems(x=>{const e=x.find(i=>i.id===f.id);return e?x.map(i=>i.id===f.id?{...i,qty:i.qty+1}:i):[...x,{...f,qty:1}]});const remove=(id:string)=>setItems(x=>x.filter(i=>i.id!==id));const v=useMemo(()=>({items,add,remove,total:items.reduce((s,i)=>s+i.price*i.qty,0),count:items.reduce((s,i)=>s+i.qty,0)}),[items]);return <CartContext.Provider value={v}>{children}</CartContext.Provider>}
export const useCart=()=>{const c=useContext(CartContext);if(!c)throw new Error('useCart must be inside CartProvider');return c};
