package com.example.questroomdatabase_0118

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import com.example.questroomdatabase_0118.ui.theme.QuestRoomDatabase_0118Theme
import com.example.questroomdatabase_0118.uicontroller.SiswaApp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            QuestRoomDatabase_0118Theme {
                SiswaApp()
            }
        }
    }
}
