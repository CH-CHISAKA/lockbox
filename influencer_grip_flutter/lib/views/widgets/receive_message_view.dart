import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../controllers/app_controller.dart';

class ReceiveMessageView extends StatefulWidget {
  const ReceiveMessageView({super.key});

  @override
  State<ReceiveMessageView> createState() => _ReceiveMessageViewState();
}

class _ReceiveMessageViewState extends State<ReceiveMessageView> {
  final TextEditingController _encryptedMessageController = TextEditingController();
  final TextEditingController _keyController = TextEditingController();
  String _decryptedMessage = '';
  bool _isDecrypting = false;

  @override
  void dispose() {
    _encryptedMessageController.dispose();
    _keyController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Receive & Decrypt Message',
          style: Theme.of(context).textTheme.headlineMedium?.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),

        const SizedBox(height: 32),

        // Encrypted message input
        TextField(
          controller: _encryptedMessageController,
          decoration: InputDecoration(
            labelText: 'Encrypted Message',
            labelStyle: const TextStyle(color: Colors.white70),
            hintText: 'Paste the encrypted message here',
            hintStyle: const TextStyle(color: Colors.white38),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
            ),
            filled: true,
            fillColor: const Color(0xFF141A20),
          ),
          style: const TextStyle(color: Colors.white),
          maxLines: 4,
        ),

        const SizedBox(height: 16),

        // Decryption key input
        TextField(
          controller: _keyController,
          decoration: InputDecoration(
            labelText: 'Decryption Key',
            labelStyle: const TextStyle(color: Colors.white70),
            hintText: 'Enter the decryption key',
            hintStyle: const TextStyle(color: Colors.white38),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
            ),
            filled: true,
            fillColor: const Color(0xFF141A20),
          ),
          style: const TextStyle(color: Colors.white),
          obscureText: true,
        ),

        const SizedBox(height: 24),

        // Decrypt button
        SizedBox(
          width: double.infinity,
          child: ElevatedButton(
            onPressed: _isDecrypting ? null : _decryptMessage,
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF508CA4),
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 16),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            child: _isDecrypting
                ? const SizedBox(
                    width: 20,
                    height: 20,
                    child: CircularProgressIndicator(
                      strokeWidth: 2,
                      valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                    ),
                  )
                : const Text('Decrypt Message'),
          ),
        ),

        if (_decryptedMessage.isNotEmpty) ...[
          const SizedBox(height: 24),

          // Decrypted message display
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: const Color(0xFF141A20),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: const Color(0xFF0A8754)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.lock_open, color: Color(0xFF0A8754)),
                    const SizedBox(width: 8),
                    Text(
                      'Decrypted Message',
                      style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        color: Colors.white,
                      ),
                    ),
                    const Spacer(),
                    IconButton(
                      onPressed: () {
                        // Copy decrypted message to clipboard
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text('Decrypted message copied to clipboard'),
                          ),
                        );
                      },
                      icon: const Icon(Icons.copy, color: Colors.white70),
                      tooltip: 'Copy to clipboard',
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Text(
                  _decryptedMessage,
                  style: const TextStyle(
                    color: Colors.white,
                    fontSize: 16,
                  ),
                ),
              ],
            ),
          ),
        ],
      ],
    );
  }

  void _decryptMessage() async {
    final encryptedMessage = _encryptedMessageController.text.trim();
    final key = _keyController.text.trim();

    if (encryptedMessage.isEmpty) {
      _showError('Please enter an encrypted message');
      return;
    }

    if (key.isEmpty || key.length < 16) {
      _showError('Please enter a valid decryption key (min 16 characters)');
      return;
    }

    setState(() {
      _isDecrypting = true;
    });

    try {
      final controller = context.read<AppController>();
      final decrypted = controller.decryptMessage(encryptedMessage, key);

      setState(() {
        _decryptedMessage = decrypted;
      });
    } catch (e) {
      _showError('Decryption failed: $e');
    } finally {
      setState(() {
        _isDecrypting = false;
      });
    }
  }

  void _showError(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        backgroundColor: Colors.red,
      ),
    );
  }
}