import 'package:flutter/material.dart';
import '../../models/influencer.dart';
import '../../utils/formatters.dart';
import '../widgets/avatar.dart';

class InfluencerCard extends StatelessWidget {
  const InfluencerCard({super.key, required this.profile});
  final InfluencerProfile profile;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: 180,
      padding: const EdgeInsets.all(12),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFE6E8EC)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              const Avatar(size: 42),
              const SizedBox(width: 8),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(profile.name, maxLines: 1, overflow: TextOverflow.ellipsis, style: const TextStyle(fontWeight: FontWeight.w600)),
                    Text('@${profile.username}', style: const TextStyle(fontSize: 12, color: Colors.grey)),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 8),
          Wrap(
            spacing: 6,
            runSpacing: -8,
            children: profile.categories.take(3).map((c) => Chip(label: Text(c))).toList(),
          ),
          const Spacer(),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(formatCompactNumber(profile.reach), style: const TextStyle(fontWeight: FontWeight.w700)),
                  const Text('Reach', style: TextStyle(fontSize: 12, color: Colors.grey)),
                ],
              ),
              Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('${(profile.engagementRate * 100).toStringAsFixed(1)}%', style: const TextStyle(fontWeight: FontWeight.w700)),
                  const Text('Engagement', style: TextStyle(fontSize: 12, color: Colors.grey)),
                ],
              ),
            ],
          ),
          const SizedBox(height: 8),
          FilledButton(
            onPressed: () {},
            child: Text('From ${formatMoney(profile.ratePerPost)}'),
          ),
        ],
      ),
    );
  }
}
