import 'package:flutter/material.dart';

class AboutView extends StatelessWidget {
  const AboutView({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          'About InfluencerGrip',
          style: Theme.of(context).textTheme.headlineMedium?.copyWith(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),

        const SizedBox(height: 32),

        // App description
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: const Color(0xFF141A20),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                'InfluencerGrip is a secure messaging application designed for encrypted communications with advanced security features.',
                style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                  color: Colors.white70,
                ),
              ),

              const SizedBox(height: 24),

              Text(
                'Key Features:',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),

              const SizedBox(height: 16),

              _buildFeatureList(),

              const SizedBox(height: 24),

              Text(
                'Security & Privacy:',
                style: Theme.of(context).textTheme.titleLarge?.copyWith(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                ),
              ),

              const SizedBox(height: 16),

              _buildSecurityList(),

              const SizedBox(height: 24),

              Text(
                'Version: 1.0.0',
                style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Colors.white60,
                ),
              ),

              const SizedBox(height: 8),

              Text(
                'Built with Flutter & Dart',
                style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                  color: Colors.white60,
                ),
              ),
            ],
          ),
        ),

        const SizedBox(height: 32),

        // Developer info or additional content
        Container(
          padding: const EdgeInsets.all(20),
          decoration: BoxDecoration(
            color: const Color(0xFF141A20),
            borderRadius: BorderRadius.circular(12),
          ),
          child: Row(
            children: [
              const Icon(
                Icons.security,
                color: Color(0xFF0A8754),
                size: 48,
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      'Your Security Matters',
                      style: Theme.of(context).textTheme.titleLarge?.copyWith(
                        color: Colors.white,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    const SizedBox(height: 8),
                    Text(
                      'This application prioritizes your privacy and security. All communications are encrypted using industry-standard AES-256 encryption.',
                      style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                        color: Colors.white70,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ],
    );
  }

  Widget _buildFeatureList() {
    final features = [
      '• End-to-end encryption with AES-256',
      '• Secure OTP verification via SMS',
      '• Network device discovery and management',
      '• Real-time message encryption/decryption',
      '• Cross-platform compatibility',
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: features.map((feature) {
        return Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Row(
            children: [
              const Icon(Icons.check, color: Color(0xFF0A8754), size: 20),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  feature,
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                ),
              ),
            ],
          ),
        );
      }).toList(),
    );
  }

  Widget _buildSecurityList() {
    final securityFeatures = [
      '• AES-256 encryption for all messages',
      '• Secure key generation and management',
      '• OTP-based authentication',
      '• Network security protocols',
      '• Local data protection',
    ];

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: securityFeatures.map((feature) {
        return Padding(
          padding: const EdgeInsets.only(bottom: 8),
          child: Row(
            children: [
              const Icon(Icons.shield, color: Color(0xFF508CA4), size: 20),
              const SizedBox(width: 8),
              Expanded(
                child: Text(
                  feature,
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                ),
              ),
            ],
          ),
        );
      }).toList(),
    );
  }
}