import { StyleSheet, Text, View } from 'react-native';


const Envmonitor = () => {
    return(
        <View style={styles.envStyle}>
            <View style={styles.dashboard}>
                <Text style={styles.textDashboard}>Environment Monitoring</Text>
            </View>
            <View>
                <Text>Intensitas cahaya</Text>
                <View style={[styles.displayResult, styles.marginIC]}><Text style={styles.textStyle}>200</Text></View>
            </View>
            <View style={styles.displayBox}>
                <Text style={styles.marginHujan}>Hujan</Text>
                <Text style={styles.marginSuhu}>Suhu</Text>
            </View>
            <View style={styles.displayBox}>
                <View style={styles.displayResult}><Text style={styles.textStyle}>Ya</Text></View>
                <View style={styles.displayResult}><Text style={styles.textStyle}>30 C</Text></View>
            </View>
            <View>
                <Text>Kelembaban udara</Text>
                <View style={[styles.displayResult, styles.marginKU]}><Text style={styles.textStyle}>100 %</Text></View>
            </View>
            <View>
                <Text>Tekanan udara</Text>
                <View style={[styles.displayResult, styles.marginTU]}><Text style={styles.textStyle}>12 hPa</Text></View>
            </View>
            <View>
                <Text>Kelembaban tanah</Text>
                <View style={[styles.displayResult, styles.marginTN]}><Text style={styles.textStyle}>100 %</Text></View>
            </View>
            <View style={[styles.displayBox, styles.marginPeriodeBox]}>
                <Text>Periode :</Text>
                <View style={[styles.displayResult, styles.marginPeriode]}><Text style={styles.textStyle}>Harian</Text></View>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    dashboard: {
      width: 425,
      height: 80,
      backgroundColor: "#f15a3b",
      padding: 20,
      justifyContent: "center",
      borderBottomLeftRadius: 15,
      borderBottomRightRadius: 15,
      marginBottom: 20,
    },
    textDashboard: {
      fontSize: 20,
      color: "white",
      marginLeft: 90,
      fontWeight: 'bold',
    },
    displayBox: {
      display: 'flex',
      flexDirection: "row",
    },
    displayResult: {
      backgroundColor: '#27194c',
      width: 55,
      borderRadius: 5,
      margin: 5,
      padding: 5,
      alignItems: 'center',
    },
    textStyle: {
      color: '#ab7a60',
    },
    envStyle: {
      justifyContent: 'center',
      alignItems: 'center',
    },
    marginSuhu: {
      marginLeft: 15,
    },
    marginHujan: {
      marginRight: 15,
    },
    marginIC: {
      marginLeft: 25,
    },
    marginKU: {
      marginLeft: 30,
    },
    marginTU: {
      marginLeft: 18,
    },
    marginTN: {
      marginLeft: 30,
    },
    marginPeriode: {
      marginLeft: 15,
      marginTop: 0,
    },
    marginPeriodeBox: {
      marginTop: 30,
    }
});

export default Envmonitor;