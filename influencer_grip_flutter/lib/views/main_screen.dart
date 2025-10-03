import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../controllers/app_controller.dart';
import 'widgets/sidebar.dart';
import 'widgets/central_area.dart';

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  @override
  void initState() {
    super.initState();
    // Request SMS permissions on app start
    WidgetsBinding.instance.addPostFrameCallback((_) {
      context.read<AppController>().discoverDevices();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
            colors: [
              Color(0xFF141A20),
              Color(0xFF212A34),
            ],
          ),
        ),
        child: Row(
          children: [
            const Sidebar(), // Sidebar with navigation buttons
            Expanded(
              child: Consumer<AppController>(
                builder: (context, controller, child) {
                  return CentralArea(
                    currentView: controller.currentView,
                    serverRunning: controller.serverRunning,
                    isLoading: controller.isLoading,
                    discoveredDevices: controller.discoveredDevices,
                  );
                },
              ),
            ),
          ],
        ),
      ),
    );
  }
}