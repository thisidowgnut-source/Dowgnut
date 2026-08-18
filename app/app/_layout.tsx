import { Stack } from 'expo-router';
import { CartProvider } from '../src/CartContext';

export default function Layout() {
  return (
    <CartProvider>
      <Stack screenOptions={{ headerShown: false }} />
    </CartProvider>
  );
}
