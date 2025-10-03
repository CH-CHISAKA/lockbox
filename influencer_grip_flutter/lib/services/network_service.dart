import 'dart:async';
import 'dart:io';
import '../models/network_device.dart';
import '../models/encryption_settings.dart';

class NetworkService {
  ServerSocket? _server;
  final List<Socket> _clients = [];
  final ServerSettings _serverSettings = const ServerSettings();
  Timer? _discoveryTimer;

  ServerSettings get serverSettings => _serverSettings;

  Future<void> startServer() async {
    try {
      _server = await ServerSocket.bind(
        InternetAddress.anyIPv4,
        _serverSettings.port,
        shared: true,
      );

      print('Server started on port ${_serverSettings.port}');

      _server!.listen((Socket client) {
        _handleClient(client);
      });
    } catch (e) {
      print('Failed to start server: $e');
      throw Exception('Failed to start server: $e');
    }
  }

  Future<void> stopServer() async {
    try {
      for (var client in _clients) {
        await client.close();
      }
      _clients.clear();

      await _server?.close();
      _server = null;

      print('Server stopped');
    } catch (e) {
      print('Failed to stop server: $e');
      throw Exception('Failed to stop server: $e');
    }
  }

  void _handleClient(Socket client) {
    print('Client connected: ${client.remoteAddress.address}:${client.remotePort}');
    _clients.add(client);

    client.listen(
      (data) {
        // Handle incoming data
        print('Received data from client');
      },
      onDone: () {
        print('Client disconnected: ${client.remoteAddress.address}:${client.remotePort}');
        _clients.remove(client);
        client.close();
      },
      onError: (error) {
        print('Client error: $error');
        _clients.remove(client);
        client.close();
      },
    );
  }

  Future<List<NetworkDevice>> discoverDevices() async {
    List<NetworkDevice> devices = [];

    try {
      // Get local network interfaces
      for (var interface in await NetworkInterface.list()) {
        for (var address in interface.addresses) {
          if (address.type == InternetAddressType.IPv4) {
            // Scan local subnet
            final subnet = _getSubnet(address.address);
            for (int i = 1; i < 255; i++) {
              final host = '$subnet$i';
              if (await _isHostReachable(host)) {
                devices.add(NetworkDevice(
                  id: host,
                  name: 'Device $i',
                  ipAddress: host,
                  port: _serverSettings.port,
                  isOnline: true,
                  type: DeviceType.unknown,
                ));
              }
            }
          }
        }
      }
    } catch (e) {
      print('Error discovering devices: $e');
    }

    return devices;
  }

  Future<bool> _isHostReachable(String host) async {
    try {
      final socket = await Socket.connect(host, _serverSettings.port,
          timeout: const Duration(milliseconds: 500));
      await socket.close();
      return true;
    } catch (e) {
      return false;
    }
  }

  String _getSubnet(String ipAddress) {
    final parts = ipAddress.split('.');
    if (parts.length == 4) {
      return '${parts[0]}.${parts[1]}.${parts[2]}.';
    }
    return ipAddress;
  }

  void startPeriodicDiscovery(Duration interval) {
    _discoveryTimer?.cancel();
    _discoveryTimer = Timer.periodic(interval, (timer) {
      discoverDevices();
    });
  }

  void stopPeriodicDiscovery() {
    _discoveryTimer?.cancel();
    _discoveryTimer = null;
  }

  void dispose() {
    stopPeriodicDiscovery();
    stopServer();
  }
}