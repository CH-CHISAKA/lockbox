import 'package:flutter/material.dart';
import '../../models/network_device.dart';
import 'home_view.dart';
import 'send_message_view.dart';
import 'receive_message_view.dart';
import 'about_view.dart';

class CentralArea extends StatelessWidget {
  final String currentView;
  final bool serverRunning;
  final bool isLoading;
  final List<NetworkDevice> discoveredDevices;

  const CentralArea({
    super.key,
    required this.currentView,
    required this.serverRunning,
    required this.isLoading,
    required this.discoveredDevices,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: const Color(0xFF212A34),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: _getCurrentView(),
      ),
    );
  }

  Widget _getCurrentView() {
    switch (currentView) {
      case 'home':
        return HomeView(
          serverRunning: serverRunning,
          isLoading: isLoading,
          discoveredDevices: discoveredDevices,
        );
      case 'send':
        return const SendMessageView();
      case 'receive':
        return const ReceiveMessageView();
      case 'about':
        return const AboutView();
      default:
        return HomeView(
          serverRunning: serverRunning,
          isLoading: isLoading,
          discoveredDevices: discoveredDevices,
        );
    }
  }
}