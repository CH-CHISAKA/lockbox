import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'controllers/app_controller.dart';
import 'views/main_screen.dart';

void main() {
  runApp(const InfluencerGripApp());
}

class InfluencerGripApp extends StatelessWidget {
  const InfluencerGripApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AppController()),
      ],
      child: MaterialApp(
        title: 'InfluencerGrip',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(
            seedColor: const Color(0xFF508CA4),
            brightness: Brightness.dark,
          ),
          useMaterial3: true,
          fontFamily: 'Ubuntu',
          scaffoldBackgroundColor: const Color(0xFF141A20),
        ),
        home: const MainScreen(),
        debugShowCheckedModeBanner: false,
      ),
    );
  }
}