class NetworkDevice {
  final String id;
  final String name;
  final String ipAddress;
  final int port;
  final bool isOnline;
  final DeviceType type;

  NetworkDevice({
    required this.id,
    required this.name,
    required this.ipAddress,
    required this.port,
    required this.isOnline,
    required this.type,
  });

  factory NetworkDevice.fromJson(Map<String, dynamic> json) {
    return NetworkDevice(
      id: json['id'],
      name: json['name'],
      ipAddress: json['ipAddress'],
      port: json['port'],
      isOnline: json['isOnline'],
      type: DeviceType.values[json['type']],
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'name': name,
      'ipAddress': ipAddress,
      'port': port,
      'isOnline': isOnline,
      'type': type.index,
    };
  }
}

enum DeviceType {
  mobile,
  desktop,
  server,
  unknown,
}