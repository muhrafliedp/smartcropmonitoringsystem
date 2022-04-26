import React, { useState } from 'react';
import { StyleSheet, Text, View, Pressable, Picker } from 'react-native';

const DaftarTanaman = () => {
    return(
        <View style={{alignItems: 'center'}}>
            <Text style={{fontSize: 20, color: '#27194c'}}>Tanaman Terbaik :</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>1. Tomat</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>2. Wortel</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>3. Tanaman Rempah</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>4. Kangkung</Text>
            <View style={styles.detailBtn}>
                <Text style={{ color: '#ab7a60', fontSize: 17}}>Lihat Penjelasan</Text>
            </View>
        </View>
    )
}

const Cropsmonitor = () => {
    const [show, setShow] = useState(false);

    return(
        <View>
            <View style={styles.dashboard}>
                <Text style={styles.textDashboard}>Crop Types</Text>
            </View>
            <View style={{ justifyContent: 'center', alignItems: 'center'}}>
                <Pressable style={styles.generateBtn} onPress={()=> {setShow(!show)}}>
                    <Text style={{ color: '#ab7a60', fontSize: 20}}>Generate Best Crop</Text>
                </Pressable>
            </View>
            {show && <DaftarTanaman />}
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
          fontSize: 20,
          color: "white",
          marginLeft: 120,
          fontWeight: 'bold',
      },
    generateBtn: {
        backgroundColor: '#27194c',
        margin: 20,
        width: 110,
        padding: 10,
        borderRadius: 5,
    },
    detailBtn: {
        backgroundColor: '#27194c',
        margin: 20,
        width: 150,
        padding: 10,
        borderRadius: 5,
    }
});

export default Cropsmonitor;