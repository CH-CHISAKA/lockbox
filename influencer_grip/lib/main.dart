import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'controllers/auth_controller.dart';
import 'theme/app_theme.dart';
import 'views/screens/splash_screen.dart';
import 'views/screens/auth/sign_in_screen.dart';
import 'views/screens/home/home_shell.dart';

void main() => runApp(const InfluencerGripApp());

class InfluencerGripApp extends StatelessWidget {
  const InfluencerGripApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthController()),
      ],
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'InfluencerGrip',
        theme: AppTheme.light,
        darkTheme: AppTheme.dark,
        initialRoute: '/',
        routes: {
          '/': (_) => const SplashScreen(),
          '/sign-in': (_) => const SignInScreen(),
          '/home': (_) => const HomeShell(),
        },
      ),
    );
  }
}
