import React, { useState } from 'react';
import { StyleSheet, Text, View, Pressable, Picker } from 'react-native';


const DaftarNutrisi = () => {
    return(
        <View style={{alignItems: 'center'}}>
            <Text style={{fontSize: 20, color: '#27194c'}}>Nutrisi Terbaik :</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>1. Pupuk NPK</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>2. Pupuk Super</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>3. Larutan Urea</Text>
            <Text style={{fontSize: 15, color: '#27194c'}}>4. Multitonik Organik</Text>
            <View style={styles.detailBtn}>
                <Text style={{ color: '#ab7a60', fontSize: 17}}>Lihat Penjelasan</Text>
            </View>
        </View>
    )
}


const Nutrients = () => {
    const [selectedValue, setSelectedValue] = useState("");
    const [show, setShow] = useState(false);
    return(
        <View>
            <View style={styles.dashboard}>
                <Text style={styles.textDashboard}>Crop Nutrients</Text>
            </View>
            <View style={{ justifyContent: 'center', alignItems: 'center'}}>
                <Text style={{fontSize: 20, color: '#27194c'}}>Pilih Tanaman</Text>
            </View>
            <View style={styles.container}>
                <Picker
                    selectedValue={selectedValue}
                    style={{ height: 50, width: 150}}
                    onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
                >
                    <Picker.Item label="Padi" value="Padi" />
                    <Picker.Item label="Jagung" value="Maize" />
                    <Picker.Item label="Kentang" value="Kentang" />
                </Picker>
            </View>
            <View style={{ justifyContent: 'center', alignItems: 'center'}}>
                <Pressable style={styles.generateBtn} onPress={()=> {
                    if (selectedValue) {
                        setShow(!show);
                    }
                    else{
                        alert('Pilih tanaman terlebih dahulu!')
                    }
                }}>
                    <Text style={{ color: '#ab7a60', fontSize: 20}}>Generate</Text>
                </Pressable>
            </View>
            {show && <DaftarNutrisi />}
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
    container: {
        paddingTop: 40,
        alignItems: "center",
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

export default Nutrients;