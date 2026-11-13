package com.example.questroomdatabase_0118

import android.app.Application
import com.example.questroomdatabase_0118.repositori.ContainerApp
import com.example.questroomdatabase_0118.repositori.ContainerDataApp

class AplikasiSiswa : Application() {
    /**
     * AppContainer instance digunakan oleh kelas-kelas lainnya untuk mendapatkan dependensi
     */
    lateinit var container: ContainerApp

    override fun onCreate() {
        super.onCreate()
        container = ContainerDataApp(this)
    }
}
