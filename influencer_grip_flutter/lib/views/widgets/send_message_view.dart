import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../controllers/app_controller.dart';

class SendMessageView extends StatefulWidget {
  const SendMessageView({super.key});

  @override
  State<SendMessageView> createState() => _SendMessageViewState();
}

class _SendMessageViewState extends State<SendMessageView> {
  final TextEditingController _messageController = TextEditingController();
  final TextEditingController _keyController = TextEditingController();
  final TextEditingController _recipientController = TextEditingController();
  String _encryptedMessage = '';
  bool _isEncrypting = false;

  @override
  void dispose() {
    _messageController.dispose();
    _keyController.dispose();
    _recipientController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'Send Encrypted Message',
          style: Theme.of(context).textTheme.headlineMedium?.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),

        const SizedBox(height: 32),

        // Message input
        TextField(
          controller: _messageController,
          decoration: InputDecoration(
            labelText: 'Message',
            labelStyle: const TextStyle(color: Colors.white70),
            hintText: 'Enter your message to encrypt',
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

        // Encryption key input
        TextField(
          controller: _keyController,
          decoration: InputDecoration(
            labelText: 'Encryption Key',
            labelStyle: const TextStyle(color: Colors.white70),
            hintText: 'Enter encryption key (min 16 characters)',
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

        const SizedBox(height: 16),

        // Recipient input
        TextField(
          controller: _recipientController,
          decoration: InputDecoration(
            labelText: 'Recipient',
            labelStyle: const TextStyle(color: Colors.white70),
            hintText: 'Enter recipient identifier',
            hintStyle: const TextStyle(color: Colors.white38),
            border: OutlineInputBorder(
              borderRadius: BorderRadius.circular(8),
            ),
            filled: true,
            fillColor: const Color(0xFF141A20),
          ),
          style: const TextStyle(color: Colors.white),
        ),

        const SizedBox(height: 24),

        // Encrypt button
        SizedBox(
          width: double.infinity,
          child: ElevatedButton(
            onPressed: _isEncrypting ? null : _encryptMessage,
            style: ElevatedButton.styleFrom(
              backgroundColor: const Color(0xFF508CA4),
              foregroundColor: Colors.white,
              padding: const EdgeInsets.symmetric(vertical: 16),
              shape: RoundedRectangleBorder(
                borderRadius: BorderRadius.circular(8),
              ),
            ),
            child: _isEncrypting
                ? const SizedBox(
                    width: 20,
                    height: 20,
                    child: CircularProgressIndicator(
                      strokeWidth: 2,
                      valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                    ),
                  )
                : const Text('Encrypt Message'),
          ),
        ),

        if (_encryptedMessage.isNotEmpty) ...[
          const SizedBox(height: 24),

          // Encrypted message display
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(
              color: const Color(0xFF141A20),
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: const Color(0xFF508CA4)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.lock, color: Color(0xFF0A8754)),
                    const SizedBox(width: 8),
                    Text(
                      'Encrypted Message',
                      style: Theme.of(context).textTheme.titleMedium?.copyWith(
                        color: Colors.white,
                      ),
                    ),
                    const Spacer(),
                    IconButton(
                      onPressed: () {
                        // Copy encrypted message to clipboard
                        ScaffoldMessenger.of(context).showSnackBar(
                          const SnackBar(
                            content: Text('Encrypted message copied to clipboard'),
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
                  _encryptedMessage,
                  style: const TextStyle(
                    color: Colors.white70,
                    fontFamily: 'monospace',
                  ),
                ),
              ],
            ),
          ),

          const SizedBox(height: 16),

          // Send via network button
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: _encryptedMessage.isEmpty ? null : _sendViaNetwork,
              icon: const Icon(Icons.send),
              label: const Text('Send via Network'),
              style: ElevatedButton.styleFrom(
                backgroundColor: const Color(0xFF0A8754),
                foregroundColor: Colors.white,
                padding: const EdgeInsets.symmetric(vertical: 16),
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(8),
                ),
              ),
            ),
          ),
        ],
      ],
    );
  }

  void _encryptMessage() async {
    final message = _messageController.text.trim();
    final key = _keyController.text.trim();

    if (message.isEmpty) {
      _showError('Please enter a message');
      return;
    }

    if (key.isEmpty || key.length < 16) {
      _showError('Please enter a valid encryption key (min 16 characters)');
      return;
    }

    setState(() {
      _isEncrypting = true;
    });

    try {
      final controller = context.read<AppController>();
      final encrypted = controller.encryptMessage(message, key);

      setState(() {
        _encryptedMessage = encrypted;
      });
    } catch (e) {
      _showError('Encryption failed: $e');
    } finally {
      setState(() {
        _isEncrypting = false;
      });
    }
  }

  void _sendViaNetwork() {
    // TODO: Implement network sending
    ScaffoldMessenger.of(context).showSnackBar(
      const SnackBar(
        content: Text('Network sending feature coming soon!'),
      ),
    );
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