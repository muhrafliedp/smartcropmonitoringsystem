import React, { useState } from 'react';
import { StyleSheet, Text, View, Pressable } from 'react-native';
import { StatusBar } from 'expo-status-bar';
import { Colors } from 'react-native/Libraries/NewAppScreen';

const Dashboard = props => {
  
  const onPress = () => {
    props.navigation.navigate('EM');
  };

  const onPressNutrients = () => {
    props.navigation.navigate('NR');
  }

  const onPressCrops = () => {
    props.navigation.navigate('CR');
  }

    return(
        <View>
            <View style={styles.dashboard}>
                <Text style={styles.textDashboard}>Dashboard</Text>
            </View>
            <Pressable style={styles.button} onPress={onPress}>
                <Text style={styles.buttonText}>Environtment Monitoring</Text>
            </Pressable>
            <Pressable style={styles.button} onPress={onPressNutrients}>
                <Text style={styles.buttonText}>Nutrients Recommendations</Text>
            </Pressable>
            <Pressable style={styles.button} onPress={onPressCrops}>
                <Text style={styles.buttonText}>Crop Recommendations</Text>
            </Pressable>
               
        </View>
    )
}


const styles = StyleSheet.create({
    dashboard: {
      width: 425,
      height: 80,
      backgroundColor: "#f15a3b",
      marginRight: 10,
      padding: 20,
      justifyContent: "center",
      borderBottomLeftRadius: 15,
      borderBottomRightRadius: 15,
      marginBottom: 20,
    },
    textDashboard: {
      fontSize: 28,
      color: "white",
      marginLeft: 130,
      fontWeight: 'bold',
    },
    button: {
      padding: 20,
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: '#e0e0e0',
      margin: 15,
      width: 280,
      marginLeft: 80,
      borderRadius: 10,
    },
    buttonText: {
      fontSize: 16,
      lineHeight: 21,
      letterSpacing: 0.25,
    }
  });
  
export default Dashboard;