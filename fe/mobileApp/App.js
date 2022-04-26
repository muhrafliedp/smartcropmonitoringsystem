import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import Dashboard from './components/Dashboard';
import Envmonitor from './components/Envmonitor';
import Nutrients from './components/Nutrients';
import Cropsmonitor from './components/Cropsmonitor';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

export default function App() {

  const Stack = createNativeStackNavigator();

  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Homescreen"
          component={Dashboard}
        />
        <Stack.Screen
          name="EM"
          component={Envmonitor}
          />
        <Stack.Screen
          name="NR"
          component={Nutrients}
          />
        <Stack.Screen
          name="CR"
          component={Cropsmonitor}
          />
      </Stack.Navigator>
   </NavigationContainer>
  );
}

