import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../../../../controllers/profile_controller.dart';
import '../../../../views/widgets/avatar.dart';

class ProfileTab extends StatelessWidget {
  const ProfileTab({super.key});

  @override
  Widget build(BuildContext context) {
    final controller = context.watch<ProfileController>();
    final user = controller.user;

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        Row(
          children: [
            const Avatar(size: 64),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(user.fullName, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w700)),
                  const SizedBox(height: 4),
                  Text('@${user.username}', style: const TextStyle(color: Colors.grey)),
                ],
              ),
            ),
            FilledButton.tonal(onPressed: () {}, child: const Text('Edit')),
          ],
        ),
        const SizedBox(height: 16),
        Row(
          children: [
            _Metric(label: 'Followers', value: user.followers.toString()),
            const SizedBox(width: 16),
            _Metric(label: 'Following', value: user.following.toString()),
          ],
        ),
        const SizedBox(height: 16),
        const Text('Bio', style: TextStyle(fontWeight: FontWeight.w600)),
        const SizedBox(height: 8),
        Text(user.bio),
      ],
    );
  }
}

class _Metric extends StatelessWidget {
  const _Metric({required this.label, required this.value});
  final String label;
  final String value;

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12),
        decoration: BoxDecoration(
          color: Theme.of(context).colorScheme.surface,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: const Color(0xFFE6E8EC)),
        ),
        child: Column(
          children: [
            Text(value, style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 16)),
            const SizedBox(height: 4),
            Text(label, style: const TextStyle(color: Colors.grey)),
          ],
        ),
      ),
    );
  }
}
