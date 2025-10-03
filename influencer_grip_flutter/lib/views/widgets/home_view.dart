import 'package:flutter/material.dart';
import '../../models/network_device.dart';

class HomeView extends StatelessWidget {
  final bool serverRunning;
  final bool isLoading;
  final List<NetworkDevice> discoveredDevices;

  const HomeView({
    super.key,
    required this.serverRunning,
    required this.isLoading,
    required this.discoveredDevices,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Welcome text
        Text(
          'Welcome to InfluencerGrip',
          style: Theme.of(context).textTheme.headlineMedium?.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),

        const SizedBox(height: 16),

        Text(
          'Your secure messaging companion for encrypted communications.',
          style: Theme.of(context).textTheme.bodyLarge?.copyWith(
            color: Colors.white70,
          ),
        ),

        const SizedBox(height: 32),

        // Features section
        Text(
          'Features:',
          style: Theme.of(context).textTheme.titleLarge?.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),

        const SizedBox(height: 16),

        _buildFeatureList(),

        const SizedBox(height: 32),

        // Server status
        _buildServerStatus(),

        const SizedBox(height: 32),

        // Discovered devices
        if (discoveredDevices.isNotEmpty) ...[
          Text(
            'Discovered Devices:',
            style: Theme.of(context).textTheme.titleLarge?.copyWith(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),

          const SizedBox(height: 16),

          _buildDeviceList(),
        ],
      ],
    );
  }

  Widget _buildFeatureList() {
    final features = [
      '• End-to-end encryption with AES-256',
      '• Secure OTP verification via SMS',
      '• Network device discovery',
      '• Real-time message encryption/decryption',
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: features.map((feature) {
        return Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Text(
            feature,
            style: const TextStyle(
              color: Colors.white70,
              fontSize: 16,
            ),
          ),
        );
      }).toList(),
    );
  }

  Widget _buildServerStatus() {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: serverRunning
            ? const Color(0xFF0A8754).withOpacity(0.2)
            : const Color(0xFFB22222).withOpacity(0.2),
        borderRadius: BorderRadius.circular(8),
        border: Border.all(
          color: serverRunning
              ? const Color(0xFF0A8754)
              : const Color(0xFFB22222),
        ),
      ),
      child: Row(
        children: [
          Icon(
            serverRunning ? Icons.check_circle : Icons.error,
            color: serverRunning
                ? const Color(0xFF0A8754)
                : const Color(0xFFB22222),
          ),
          const SizedBox(width: 12),
          Text(
            serverRunning
                ? 'Server is running on port 8080'
                : 'Server is not running',
            style: TextStyle(
              color: serverRunning ? Colors.white : Colors.white70,
              fontSize: 16,
            ),
          ),
          if (isLoading) ...[
            const SizedBox(width: 12),
            const SizedBox(
              width: 16,
              height: 16,
              child: CircularProgressIndicator(
                strokeWidth: 2,
                valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
              ),
            ),
          ],
        ],
      ),
    );
  }

  Widget _buildDeviceList() {
    return Expanded(
      child: Container(
        decoration: BoxDecoration(
          color: const Color(0xFF141A20),
          borderRadius: BorderRadius.circular(8),
        ),
        child: ListView.builder(
          itemCount: discoveredDevices.length,
          itemBuilder: (context, index) {
            final device = discoveredDevices[index];
            return ListTile(
              leading: CircleAvatar(
                backgroundColor: device.isOnline
                    ? const Color(0xFF0A8754)
                    : Colors.grey,
                child: Icon(
                  _getDeviceIcon(device.type),
                  color: Colors.white,
                  size: 20,
                ),
              ),
              title: Text(
                device.name,
                style: const TextStyle(color: Colors.white),
              ),
              subtitle: Text(
                '${device.ipAddress}:${device.port}',
                style: const TextStyle(color: Colors.white70),
              ),
              trailing: Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
                decoration: BoxDecoration(
                  color: device.isOnline
                      ? const Color(0xFF0A8754).withOpacity(0.2)
                      : Colors.grey.withOpacity(0.2),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Text(
                  device.isOnline ? 'Online' : 'Offline',
                  style: TextStyle(
                    color: device.isOnline ? Colors.white : Colors.white70,
                    fontSize: 12,
                  ),
                ),
              ),
            );
          },
        ),
      ),
    );
  }

  IconData _getDeviceIcon(DeviceType type) {
    switch (type) {
      case DeviceType.mobile:
        return Icons.smartphone;
      case DeviceType.desktop:
        return Icons.computer;
      case DeviceType.server:
        return Icons.dns;
      default:
        return Icons.device_unknown;
    }
  }
}