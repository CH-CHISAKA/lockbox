import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../controllers/app_controller.dart';

class Sidebar extends StatelessWidget {
  const Sidebar({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<AppController>();

    return Container(
      width: 200,
      decoration: BoxDecoration(
        gradient: const LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [
            Color(0xFF8091AB),
            Color(0xFF4C5C6D),
          ],
        ),
        borderRadius: BorderRadius.circular(12),
      ),
      margin: const EdgeInsets.all(16),
      child: Column(
        children: [
          const SizedBox(height: 20),
          // Server control section
          Container(
            margin: const EdgeInsets.symmetric(horizontal: 16),
            child: Column(
              children: [
                Row(
                  children: [
                    Expanded(
                      child: ElevatedButton(
                        onPressed: controller.isLoading
                            ? null
                            : () async {
                                if (controller.serverRunning) {
                                  await controller.stopServer();
                                } else {
                                  await controller.startServer();
                                }
                              },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: controller.serverRunning
                              ? const Color(0xFF0A8754)
                              : const Color(0xFF508CA4),
                          foregroundColor: Colors.white,
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(8),
                          ),
                        ),
                        child: Text(
                          controller.serverRunning ? 'Stop Server' : 'Start Server',
                        ),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Container(
                      width: 16,
                      height: 16,
                      decoration: BoxDecoration(
                        color: controller.serverRunning
                            ? const Color(0xFF0A8754)
                            : const Color(0xFFB22222),
                        borderRadius: BorderRadius.circular(8),
                        border: Border.all(color: Colors.white30),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 10),
              ],
            ),
          ),

          const SizedBox(height: 20),

          // Navigation buttons
          _buildNavButton(
            context,
            'Home',
            Icons.home,
            controller.currentView == 'home',
            () => controller.navigateToView('home'),
          ),

          _buildNavButton(
            context,
            'Send Message',
            Icons.send,
            controller.currentView == 'send',
            () => controller.navigateToView('send'),
          ),

          _buildNavButton(
            context,
            'Receive Message',
            Icons.inbox,
            controller.currentView == 'receive',
            () => controller.navigateToView('receive'),
          ),

          const Spacer(),

          _buildNavButton(
            context,
            'About',
            Icons.info,
            controller.currentView == 'about',
            () => controller.navigateToView('about'),
          ),

          _buildNavButton(
            context,
            'Exit',
            Icons.exit_to_app,
            false,
            () => _showExitDialog(context),
          ),

          const SizedBox(height: 20),
        ],
      ),
    );
  }

  Widget _buildNavButton(
    BuildContext context,
    String text,
    IconData icon,
    bool isActive,
    VoidCallback onPressed,
  ) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
      child: ElevatedButton(
        onPressed: onPressed,
        style: ElevatedButton.styleFrom(
          backgroundColor: isActive
              ? const Color(0xFF508CA4)
              : Colors.transparent,
          foregroundColor: isActive ? Colors.white : Colors.white70,
          elevation: isActive ? 4 : 0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8),
          ),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        ),
        child: Row(
          children: [
            Icon(icon, size: 20),
            const SizedBox(width: 12),
            Text(text),
          ],
        ),
      ),
    );
  }

  void _showExitDialog(BuildContext context) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Exit App'),
          content: const Text('Are you sure you want to exit?'),
          actions: [
            TextButton(
              onPressed: () => Navigator.of(context).pop(),
              child: const Text('Cancel'),
            ),
            TextButton(
              onPressed: () {
                Navigator.of(context).pop();
                // Exit the app
                // Note: In a real app, you might want to handle cleanup here
              },
              child: const Text('Exit'),
            ),
          ],
        );
      },
    );
  }
}