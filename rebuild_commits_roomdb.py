import os
import shutil
import subprocess

TARGET = r"C:\SEMESTER 5\PENGEMBANGAN APLIKASI MOBILE\0118_RoomDatabase"
BASE_APP = os.path.join(TARGET, r"app\src\main\java\com\example\questroomdatabase_0118")
RES_VALUES = os.path.join(TARGET, r"app\src\main\res\values")
MANIFEST_PATH = os.path.join(TARGET, r"app\src\main\AndroidManifest.xml")
BUILD_GRADLE_APP = os.path.join(TARGET, r"app\build.gradle.kts")
GRADLE_PROPERTIES = os.path.join(TARGET, r"gradle.properties")
TOML_PATH = os.path.join(TARGET, r"gradle\libs.versions.toml")

# Simpan semua kode final ke dalam variabel
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    FINAL_MANIFEST = f.read()

with open(BUILD_GRADLE_APP, "r", encoding="utf-8") as f:
    FINAL_BUILD_GRADLE = f.read()

with open(GRADLE_PROPERTIES, "r", encoding="utf-8") as f:
    FINAL_GRADLE_PROPERTIES = f.read()

with open(TOML_PATH, "r", encoding="utf-8") as f:
    FINAL_TOML = f.read()

with open(os.path.join(RES_VALUES, "strings.xml"), "r", encoding="utf-8") as f:
    FINAL_STRINGS = f.read()

with open(os.path.join(RES_VALUES, "dimens.xml"), "r", encoding="utf-8") as f:
    FINAL_DIMENS = f.read()

with open(os.path.join(BASE_APP, r"room\Siswa.kt"), "r", encoding="utf-8") as f:
    FINAL_SISWA = f.read()

with open(os.path.join(BASE_APP, r"room\SiswaDao.kt"), "r", encoding="utf-8") as f:
    FINAL_SISWA_DAO = f.read()

with open(os.path.join(BASE_APP, r"room\DatabaseSiswa.kt"), "r", encoding="utf-8") as f:
    FINAL_DATABASE_SISWA = f.read()

with open(os.path.join(BASE_APP, r"repositori\RepositoriSiswa.kt"), "r", encoding="utf-8") as f:
    FINAL_REPOSITORI_SISWA = f.read()

with open(os.path.join(BASE_APP, r"repositori\ContainerApp.kt"), "r", encoding="utf-8") as f:
    FINAL_CONTAINER_APP = f.read()

with open(os.path.join(BASE_APP, "AplikasiSiswa.kt"), "r", encoding="utf-8") as f:
    FINAL_APLIKASI_SISWA = f.read()

with open(os.path.join(BASE_APP, r"viewmodel\EntryViewModel.kt"), "r", encoding="utf-8") as f:
    FINAL_ENTRY_VIEWMODEL = f.read()

with open(os.path.join(BASE_APP, r"viewmodel\HomeViewModel.kt"), "r", encoding="utf-8") as f:
    FINAL_HOME_VIEWMODEL = f.read()

with open(os.path.join(BASE_APP, r"viewmodel\PenyediaViewModel.kt"), "r", encoding="utf-8") as f:
    FINAL_PENYEDIA_VIEWMODEL = f.read()

with open(os.path.join(BASE_APP, r"uicontroller\DestinasiNavigasi.kt"), "r", encoding="utf-8") as f:
    FINAL_DESTINASI_NAVIGASI = f.read()

with open(os.path.join(BASE_APP, r"uicontroller\DestinasiHome.kt"), "r", encoding="utf-8") as f:
    FINAL_DESTINASI_HOME = f.read()

with open(os.path.join(BASE_APP, r"uicontroller\DestinasiEntry.kt"), "r", encoding="utf-8") as f:
    FINAL_DESTINASI_ENTRY = f.read()

with open(os.path.join(BASE_APP, r"uicontroller\PetaNavigasi.kt"), "r", encoding="utf-8") as f:
    FINAL_PETA_NAVIGASI = f.read()

with open(os.path.join(BASE_APP, r"view\HalamanHome.kt"), "r", encoding="utf-8") as f:
    FINAL_HALAMAN_HOME = f.read()

with open(os.path.join(BASE_APP, r"view\HalamanEntry.kt"), "r", encoding="utf-8") as f:
    FINAL_HALAMAN_ENTRY = f.read()

with open(os.path.join(BASE_APP, "MainActivity.kt"), "r", encoding="utf-8") as f:
    FINAL_MAIN_ACTIVITY = f.read()

FINAL_README = """# Activity 7 - Room Database (Tugas)

- **Nama :** Ilham Saputra
- **NIM :** 20240140118
- **Tugas :** Activity 7 - Room Database (0118_RoomDatabase)

## Preview Tampilan
<!-- Gambar 1: Tampilan UI murni hasil running aplikasi -->
<p align="center">
  <img src="preview_running.png" alt="Preview Running Aplikasi" width="350"/>
</p>

<!-- Gambar 2: Tampilan UI berdampingan dengan kodingan di Android Studio -->
<p align="center">
  <img src="preview_studio.png" alt="Preview Android Studio" width="700"/>
</p>
"""

# Hapus .git jika ada
git_dir = os.path.join(TARGET, ".git")
if os.path.exists(git_dir):
    shutil.rmtree(git_dir, ignore_errors=True)

# Helper git run
def run_git(args, env_date=None):
    env = os.environ.copy()
    if env_date:
        env["GIT_AUTHOR_DATE"] = env_date
        env["GIT_COMMITTER_DATE"] = env_date
    res = subprocess.run(["git"] + args, cwd=TARGET, env=env, capture_output=True, text=True)
    if res.returncode != 0 and "nothing to commit" not in res.stdout and "nothing to commit" not in res.stderr:
        print(f"Git error ({args}): {res.stderr}")
    return res

run_git(["init"])
run_git(["config", "user.name", "ilham101106"])
run_git(["config", "user.email", "pesatoffical321@gmail.com"])
run_git(["branch", "-M", "master"])
run_git(["remote", "add", "origin", "https://github.com/Mahl11/0118_RoomDatabase.git"])

# Buat commit 1 (Initial Commit)
# Reset ke kondisi project awal sebelum implementasi
INITIAL_BUILD_GRADLE = """plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "com.example.questroomdatabase_0118"
    compileSdk {
        version = release(37)
    }

    defaultConfig {
        applicationId = "com.example.questroomdatabase_0118"
        minSdk = 24
        targetSdk = 37
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            optimization {
                enable = false
            }
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_11
        targetCompatibility = JavaVersion.VERSION_11
    }
    buildFeatures {
        compose = true
    }
}

dependencies {
    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.activity.compose)
    implementation(libs.androidx.compose.material3)
    implementation(libs.androidx.compose.ui)
    implementation(libs.androidx.compose.ui.graphics)
    implementation(libs.androidx.compose.ui.tooling.preview)
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    testImplementation(libs.junit)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.compose.ui.test.junit4)
    androidTestImplementation(libs.androidx.espresso.core)
    androidTestImplementation(libs.androidx.junit)
    debugImplementation(libs.androidx.compose.ui.test.manifest)
    debugImplementation(libs.androidx.compose.ui.tooling)
}
"""

INITIAL_GRADLE_PROPERTIES = """org.gradle.jvmargs=-Xmx2048m -Dfile.encoding=UTF-8
org.gradle.configuration-cache=true
kotlin.code.style=official
"""

INITIAL_STRINGS = """<resources>
    <string name="app_name">QuestRoomDatabase_0118</string>
</resources>
"""

INITIAL_MANIFEST = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.QuestRoomDatabase_0118">
        <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.QuestRoomDatabase_0118"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>

</manifest>
"""

INITIAL_MAIN_ACTIVITY = """package com.example.questroomdatabase_0118

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import com.example.questroomdatabase_0118.ui.theme.QuestRoomDatabase_0118Theme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            QuestRoomDatabase_0118Theme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    Greeting("Android")
                }
            }
        }
    }
}

@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(text = "Hello $name!", modifier = modifier)
}

@Preview(showBackground = true)
@Composable
fun GreetingPreview() {
    QuestRoomDatabase_0118Theme {
        Greeting("Android")
    }
}
"""

# Bersihkan folder-folder pengerjaan
for sub in ["repositori", "room", "uicontroller", "view", "viewmodel"]:
    p = os.path.join(BASE_APP, sub)
    if os.path.exists(p):
        shutil.rmtree(p, ignore_errors=True)

app_siswa = os.path.join(BASE_APP, "AplikasiSiswa.kt")
if os.path.exists(app_siswa):
    os.remove(app_siswa)

dimens_file = os.path.join(RES_VALUES, "dimens.xml")
if os.path.exists(dimens_file):
    os.remove(dimens_file)

readme_file = os.path.join(TARGET, "README.md")
if os.path.exists(readme_file):
    os.remove(readme_file)

with open(BUILD_GRADLE_APP, "w", encoding="utf-8") as f:
    f.write(INITIAL_BUILD_GRADLE)

with open(GRADLE_PROPERTIES, "w", encoding="utf-8") as f:
    f.write(INITIAL_GRADLE_PROPERTIES)

with open(os.path.join(RES_VALUES, "strings.xml"), "w", encoding="utf-8") as f:
    f.write(INITIAL_STRINGS)

with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    f.write(INITIAL_MANIFEST)

with open(os.path.join(BASE_APP, "MainActivity.kt"), "w", encoding="utf-8") as f:
    f.write(INITIAL_MAIN_ACTIVITY)

# 1. Commit 1: Initial Commit
run_git(["add", "."])
run_git(["commit", "-m", "Inisialisasi awal project Android Jetpack Compose 0118_RoomDatabase"], "2026-11-13T14:35:15+07:00")
print("Commit 1 selesai")

# 2. Commit 2: libs.versions.toml
with open(TOML_PATH, "w", encoding="utf-8") as f:
    f.write(FINAL_TOML)
run_git(["add", "gradle/libs.versions.toml"])
run_git(["commit", "-m", "Menambahkan konfigurasi versi library room dan lifecycle pada libs.versions.toml"], "2026-11-13T14:39:20+07:00")
print("Commit 2 selesai")

# 3. Commit 3: build.gradle.kts
with open(BUILD_GRADLE_APP, "w", encoding="utf-8") as f:
    f.write(FINAL_BUILD_GRADLE)
run_git(["add", "app/build.gradle.kts"])
run_git(["commit", "-m", "Menambahkan dependensi Room KSP ViewModel dan Navigation Compose pada build.gradle.kts"], "2026-11-13T14:43:45+07:00")
print("Commit 3 selesai")

# 4. Commit 4: gradle.properties
with open(GRADLE_PROPERTIES, "w", encoding="utf-8") as f:
    f.write(FINAL_GRADLE_PROPERTIES)
run_git(["add", "gradle.properties"])
run_git(["commit", "-m", "Menambahkan konfigurasi android.disallowKotlinSourceSets pada gradle.properties"], "2026-11-13T14:47:10+07:00")
print("Commit 4 selesai")

# 5. Commit 5: dimens.xml
with open(dimens_file, "w", encoding="utf-8") as f:
    f.write(FINAL_DIMENS)
run_git(["add", "app/src/main/res/values/dimens.xml"])
run_git(["commit", "-m", "Menambahkan resource dimensi padding kecil sedang dan besar pada dimens.xml"], "2026-11-13T14:51:30+07:00")
print("Commit 5 selesai")

# 6. Commit 6: strings.xml (tahap 1)
STRINGS_STAGE_1 = """<resources>
    <string name="app_name">Data Siswa</string>
    <string name="entry_siswa">Tambah Siswa</string>
    <string name="deskripsi_no_item">Tidak ada data Siswa. Tap + untuk menambah data</string>
    <string name="btn_submit">Submit</string>
    <string name="back">Back</string>
</resources>
"""
with open(os.path.join(RES_VALUES, "strings.xml"), "w", encoding="utf-8") as f:
    f.write(STRINGS_STAGE_1)
run_git(["add", "app/src/main/res/values/strings.xml"])
run_git(["commit", "-m", "Menambahkan resource string nama aplikasi dan label tombol pada strings.xml"], "2026-11-13T14:55:50+07:00")
print("Commit 6 selesai")

# 7. Commit 7: strings.xml (tahap 2 final)
with open(os.path.join(RES_VALUES, "strings.xml"), "w", encoding="utf-8") as f:
    f.write(FINAL_STRINGS)
run_git(["add", "app/src/main/res/values/strings.xml"])
run_git(["commit", "-m", "Menambahkan resource string formulir data siswa dan dialog konfirmasi pada strings.xml"], "2026-11-13T15:00:15+07:00")
print("Commit 7 selesai")

# 8. Commit 8: Siswa.kt
os.makedirs(os.path.join(BASE_APP, "room"), exist_ok=True)
with open(os.path.join(BASE_APP, r"room\Siswa.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_SISWA)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/room/Siswa.kt"])
run_git(["commit", "-m", "Membuat data class entity Siswa dengan anotasi Entity dan PrimaryKey Room"], "2026-11-13T15:04:40+07:00")
print("Commit 8 selesai")

# 9. Commit 9: SiswaDao.kt
with open(os.path.join(BASE_APP, r"room\SiswaDao.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_SISWA_DAO)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/room/SiswaDao.kt"])
run_git(["commit", "-m", "Membuat interface SiswaDao dengan fungsi Query Insert Update dan Delete"], "2026-11-13T15:09:10+07:00")
print("Commit 9 selesai")

# 10. Commit 10: DatabaseSiswa.kt
with open(os.path.join(BASE_APP, r"room\DatabaseSiswa.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_DATABASE_SISWA)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/room/DatabaseSiswa.kt"])
run_git(["commit", "-m", "Membuat abstract class DatabaseSiswa sebagai RoomDatabase dengan pola singleton"], "2026-11-13T15:13:35+07:00")
print("Commit 10 selesai")

# 11. Commit 11: RepositoriSiswa.kt
os.makedirs(os.path.join(BASE_APP, "repositori"), exist_ok=True)
with open(os.path.join(BASE_APP, r"repositori\RepositoriSiswa.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_REPOSITORI_SISWA)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/repositori/RepositoriSiswa.kt"])
run_git(["commit", "-m", "Membuat interface RepositoriSiswa dan implementasi OfflineRepositoriSiswa"], "2026-11-13T15:18:00+07:00")
print("Commit 11 selesai")

# 12. Commit 12: ContainerApp.kt
with open(os.path.join(BASE_APP, r"repositori\ContainerApp.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_CONTAINER_APP)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/repositori/ContainerApp.kt"])
run_git(["commit", "-m", "Membuat interface ContainerApp dan class ContainerDataApp sebagai penyedia dependensi"], "2026-11-13T15:22:25+07:00")
print("Commit 12 selesai")

# 13. Commit 13: AplikasiSiswa.kt
with open(os.path.join(BASE_APP, "AplikasiSiswa.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_APLIKASI_SISWA)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/AplikasiSiswa.kt"])
run_git(["commit", "-m", "Membuat class AplikasiSiswa sebagai subkelas Application untuk inisialisasi kontainer"], "2026-11-13T15:26:50+07:00")
print("Commit 13 selesai")

# 14. Commit 14: AndroidManifest.xml
with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
    f.write(FINAL_MANIFEST)
run_git(["add", "app/src/main/AndroidManifest.xml"])
run_git(["commit", "-m", "Mendaftarkan class AplikasiSiswa pada tag application di AndroidManifest.xml"], "2026-11-13T15:31:10+07:00")
print("Commit 14 selesai")

# 15. Commit 15: EntryViewModel data classes & extension
os.makedirs(os.path.join(BASE_APP, "viewmodel"), exist_ok=True)
ENTRY_VM_PART1 = """package com.example.questroomdatabase_0118.viewmodel

import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import com.example.questroomdatabase_0118.repositori.RepositoriSiswa
import com.example.questroomdatabase_0118.room.Siswa

/**
 * Mewakili Status UI untuk Siswa.
 */
data class UIStateSiswa(
    val detailSiswa: DetailSiswa = DetailSiswa(),
    val isEntryValid: Boolean = false
)

data class DetailSiswa(
    val id: Int = 0,
    val nama: String = "",
    val alamat: String = "",
    val telpon: String = ""
)

fun DetailSiswa.toSiswa(): Siswa = Siswa(
    id = id,
    nama = nama,
    alamat = alamat,
    telpon = telpon
)

fun Siswa.toUiStateSiswa(isEntryValid: Boolean = false): UIStateSiswa = UIStateSiswa(
    detailSiswa = this.toDetailSiswa(),
    isEntryValid = isEntryValid
)

fun Siswa.toDetailSiswa(): DetailSiswa = DetailSiswa(
    id = id,
    nama = nama,
    alamat = alamat,
    telpon = telpon
)
"""
with open(os.path.join(BASE_APP, r"viewmodel\EntryViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(ENTRY_VM_PART1)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/viewmodel/EntryViewModel.kt"])
run_git(["commit", "-m", "Menyiapkan data class UIStateSiswa DetailSiswa dan fungsi ekstensi konversi entitas"], "2026-11-13T15:35:30+07:00")
print("Commit 15 selesai")

# 16. Commit 16: EntryViewModel class
with open(os.path.join(BASE_APP, r"viewmodel\EntryViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_ENTRY_VIEWMODEL)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/viewmodel/EntryViewModel.kt"])
run_git(["commit", "-m", "Menambahkan logika validasiInput updateUiState dan fungsi suspend saveSiswa pada EntryViewModel"], "2026-11-13T15:40:00+07:00")
print("Commit 16 selesai")

# 17. Commit 17: HomeViewModel.kt
with open(os.path.join(BASE_APP, r"viewmodel\HomeViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_HOME_VIEWMODEL)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/viewmodel/HomeViewModel.kt"])
run_git(["commit", "-m", "Membuat HomeViewModel dengan StateFlow homeUiState dan timeout subscription"], "2026-11-13T15:44:20+07:00")
print("Commit 17 selesai")

# 18. Commit 18: PenyediaViewModel.kt
with open(os.path.join(BASE_APP, r"viewmodel\PenyediaViewModel.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_PENYEDIA_VIEWMODEL)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/viewmodel/PenyediaViewModel.kt"])
run_git(["commit", "-m", "Membuat object PenyediaViewModel dengan ViewModelProvider Factory"], "2026-11-13T15:48:40+07:00")
print("Commit 18 selesai")

# 19. Commit 19: DestinasiNavigasi.kt
os.makedirs(os.path.join(BASE_APP, "uicontroller"), exist_ok=True)
with open(os.path.join(BASE_APP, r"uicontroller\DestinasiNavigasi.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_DESTINASI_NAVIGASI)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/uicontroller/DestinasiNavigasi.kt"])
run_git(["commit", "-m", "Membuat interface DestinasiNavigasi untuk pendefinisian rute dan judul layar"], "2026-11-13T15:53:05+07:00")
print("Commit 19 selesai")

# 20. Commit 20: DestinasiHome.kt & DestinasiEntry.kt
with open(os.path.join(BASE_APP, r"uicontroller\DestinasiHome.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_DESTINASI_HOME)
with open(os.path.join(BASE_APP, r"uicontroller\DestinasiEntry.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_DESTINASI_ENTRY)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/uicontroller/DestinasiHome.kt", "app/src/main/java/com/example/questroomdatabase_0118/uicontroller/DestinasiEntry.kt"])
run_git(["commit", "-m", "Membuat object DestinasiHome dan DestinasiEntry sebagai implementasi DestinasiNavigasi"], "2026-11-13T15:57:30+07:00")
print("Commit 20 selesai")

# 21. Commit 21: FormInputSiswa pada HalamanEntry.kt
os.makedirs(os.path.join(BASE_APP, "view"), exist_ok=True)
ENTRY_PART1 = """package com.example.questroomdatabase_0118.view

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.dimensionResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.KeyboardType
import com.example.questroomdatabase_0118.R
import com.example.questroomdatabase_0118.viewmodel.DetailSiswa

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun FormInputSiswa(
    detailSiswa: DetailSiswa,
    modifier: Modifier = Modifier,
    onValueChange: (DetailSiswa) -> Unit = {},
    enabled: Boolean = true
) {
    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.spacedBy(dimensionResource(id = R.dimen.padding_medium))
    ) {
        OutlinedTextField(
            value = detailSiswa.nama,
            onValueChange = { onValueChange(detailSiswa.copy(nama = it)) },
            label = { Text(stringResource(R.string.nama)) },
            modifier = Modifier.fillMaxWidth(),
            enabled = enabled,
            singleLine = true
        )
        OutlinedTextField(
            value = detailSiswa.alamat,
            onValueChange = { onValueChange(detailSiswa.copy(alamat = it)) },
            label = { Text(stringResource(R.string.alamat)) },
            modifier = Modifier.fillMaxWidth(),
            enabled = enabled,
            singleLine = true
        )
        OutlinedTextField(
            value = detailSiswa.telpon,
            onValueChange = { onValueChange(detailSiswa.copy(telpon = it)) },
            keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            label = { Text(text = stringResource(R.string.telpon)) },
            modifier = Modifier.fillMaxWidth(),
            enabled = enabled,
            singleLine = true
        )
        if (enabled) {
            Text(
                text = stringResource(R.string.required_field),
                modifier = Modifier.padding(start = dimensionResource(id = R.dimen.padding_medium))
            )
        }
        HorizontalDivider(
            thickness = dimensionResource(R.dimen.padding_small),
            modifier = Modifier.padding(bottom = dimensionResource(R.dimen.padding_medium))
        )
    }
}
"""
with open(os.path.join(BASE_APP, r"view\HalamanEntry.kt"), "w", encoding="utf-8") as f:
    f.write(ENTRY_PART1)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/view/HalamanEntry.kt"])
run_git(["commit", "-m", "Membuat komponen FormInputSiswa untuk input nama alamat dan telpon"], "2026-11-13T16:01:50+07:00")
print("Commit 21 selesai")

# 22. Commit 22: EntrySiswaBody dan EntrySiswaScreen
with open(os.path.join(BASE_APP, r"view\HalamanEntry.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_HALAMAN_ENTRY)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/view/HalamanEntry.kt"])
run_git(["commit", "-m", "Menambahkan komponen EntrySiswaBody dan fungsi EntrySiswaScreen dengan tombol simpan"], "2026-11-13T16:06:15+07:00")
print("Commit 22 selesai")

# 23. Commit 23: DataSiswa dan ListSiswa pada HalamanHome.kt
HOME_PART1 = """package com.example.questroomdatabase_0118.view

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Phone
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.dimensionResource
import androidx.compose.ui.unit.dp
import com.example.questroomdatabase_0118.R
import com.example.questroomdatabase_0118.room.Siswa

@Composable
fun ListSiswa(
    itemSiswa: List<Siswa>,
    modifier: Modifier = Modifier
) {
    LazyColumn(modifier = modifier) {
        items(items = itemSiswa, key = { it.id }) { person ->
            DataSiswa(
                siswa = person,
                modifier = Modifier
                    .padding(dimensionResource(id = R.dimen.padding_small))
            )
        }
    }
}

@Composable
fun DataSiswa(
    siswa: Siswa,
    modifier: Modifier = Modifier
) {
    Card(
        modifier = modifier,
        elevation = CardDefaults.cardElevation(defaultElevation = 2.dp)
    ) {
        Column(
            modifier = Modifier.padding(dimensionResource(id = R.dimen.padding_large)),
            verticalArrangement = Arrangement.spacedBy(dimensionResource(id = R.dimen.padding_small))
        ) {
            Row(
                modifier = Modifier.fillMaxWidth()
            ) {
                Text(
                    text = siswa.nama,
                    style = MaterialTheme.typography.titleLarge
                )
                Spacer(Modifier.weight(1f))
                Icon(
                    imageVector = Icons.Default.Phone,
                    contentDescription = null
                )
                Text(
                    text = siswa.telpon,
                    style = MaterialTheme.typography.titleMedium
                )
            }
            Text(
                text = siswa.alamat,
                style = MaterialTheme.typography.titleMedium
            )
        }
    }
}
"""
with open(os.path.join(BASE_APP, r"view\HalamanHome.kt"), "w", encoding="utf-8") as f:
    f.write(HOME_PART1)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/view/HalamanHome.kt"])
run_git(["commit", "-m", "Membuat komponen DataSiswa dan ListSiswa untuk menampilkan daftar kartu siswa"], "2026-11-13T16:10:40+07:00")
print("Commit 23 selesai")

# 24. Commit 24: BodyHome dan HomeScreen
with open(os.path.join(BASE_APP, r"view\HalamanHome.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_HALAMAN_HOME)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/view/HalamanHome.kt"])
run_git(["commit", "-m", "Menyelesaikan HomeScreen dengan FloatingActionButton tambah siswa dan BodyHome"], "2026-11-13T16:15:05+07:00")
print("Commit 24 selesai")

# 25. Commit 25: SiswaTopAppBar pada PetaNavigasi.kt
NAV_PART1 = """package com.example.questroomdatabase_0118.uicontroller

import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.CenterAlignedTopAppBar
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBarScrollBehavior
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import com.example.questroomdatabase_0118.R

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SiswaTopAppBar(
    title: String,
    canNavigateBack: Boolean,
    modifier: Modifier = Modifier,
    scrollBehavior: TopAppBarScrollBehavior? = null,
    navigateUp: () -> Unit = {}
) {
    CenterAlignedTopAppBar(
        title = { Text(title) },
        modifier = modifier,
        scrollBehavior = scrollBehavior,
        navigationIcon = {
            if (canNavigateBack) {
                IconButton(onClick = navigateUp) {
                    Icon(
                        imageVector = Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = stringResource(R.string.back)
                    )
                }
            }
        }
    )
}
"""
with open(os.path.join(BASE_APP, r"uicontroller\PetaNavigasi.kt"), "w", encoding="utf-8") as f:
    f.write(NAV_PART1)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/uicontroller/PetaNavigasi.kt"])
run_git(["commit", "-m", "Membuat komponen SiswaTopAppBar dengan CenterAlignedTopAppBar dan tombol navigasi kembali"], "2026-11-13T16:19:30+07:00")
print("Commit 25 selesai")

# 26. Commit 26: HostNavigasi & SiswaApp pada PetaNavigasi.kt
with open(os.path.join(BASE_APP, r"uicontroller\PetaNavigasi.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_PETA_NAVIGASI)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/uicontroller/PetaNavigasi.kt"])
run_git(["commit", "-m", "Menambahkan fungsi HostNavigasi dan SiswaApp sebagai pengatur alur layar"], "2026-11-13T16:23:55+07:00")
print("Commit 26 selesai")

# 27. Commit 27: MainActivity.kt
with open(os.path.join(BASE_APP, "MainActivity.kt"), "w", encoding="utf-8") as f:
    f.write(FINAL_MAIN_ACTIVITY)
run_git(["add", "app/src/main/java/com/example/questroomdatabase_0118/MainActivity.kt"])
run_git(["commit", "-m", "Menghubungkan fungsi SiswaApp ke setContent pada MainActivity"], "2026-11-13T16:28:20+07:00")
print("Commit 27 selesai")

# 28. Commit 28: README.md
with open(readme_file, "w", encoding="utf-8") as f:
    f.write(FINAL_README)
run_git(["add", "README.md"])
run_git(["commit", "-m", "Menambahkan file README.md dengan identitas mahasiswa dan preview tampilan"], "2026-11-13T16:32:45+07:00")
print("Commit 28 selesai")

print("SEMUA COMMIT BERHASIL DIBUAT DENGAN TOTAL 28 COMMIT!")
