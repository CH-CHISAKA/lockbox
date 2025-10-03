import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../controllers/auth_controller.dart';
import '../../widgets/app_button.dart';
import '../../widgets/app_text_field.dart';

class SignInScreen extends StatefulWidget {
  const SignInScreen({super.key});

  @override
  State<SignInScreen> createState() => _SignInScreenState();
}

class _SignInScreenState extends State<SignInScreen> {
  final TextEditingController _email = TextEditingController();
  final TextEditingController _password = TextEditingController();

  @override
  Widget build(BuildContext context) {
    final auth = context.watch<AuthController>();

    return Scaffold(
      appBar: AppBar(title: const Text('Sign In')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const SizedBox(height: 24),
            AppTextField(hint: 'Email', controller: _email, keyboardType: TextInputType.emailAddress),
            const SizedBox(height: 12),
            AppTextField(hint: 'Password', controller: _password, obscureText: true),
            const SizedBox(height: 24),
            AppButton(
              label: auth.isLoading ? 'Signing In...' : 'Sign In',
              onPressed: auth.isLoading
                  ? null
                  : () async {
                      await context.read<AuthController>().signIn(_email.text, _password.text);
                      if (mounted) {
                        Navigator.of(context).pushReplacementNamed('/home');
                      }
                    },
            ),
          ],
        ),
      ),
    );
  }
}
