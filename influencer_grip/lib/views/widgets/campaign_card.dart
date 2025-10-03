import 'package:flutter/material.dart';
import '../../models/campaign.dart';
import '../../utils/formatters.dart';

class CampaignCard extends StatelessWidget {
  const CampaignCard({super.key, required this.campaign});
  final Campaign campaign;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.surface,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: const Color(0xFFE6E8EC)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 140,
            decoration: const BoxDecoration(
              color: Color(0xFFF0F2F5),
              borderRadius: BorderRadius.vertical(top: Radius.circular(16)),
            ),
            child: const Center(child: Icon(Icons.image, size: 48, color: Colors.grey)),
          ),
          Padding(
            padding: const EdgeInsets.all(12),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(campaign.title, style: const TextStyle(fontWeight: FontWeight.w700, fontSize: 16)),
                const SizedBox(height: 4),
                Text(campaign.brandName, style: const TextStyle(color: Colors.grey)),
                const SizedBox(height: 8),
                Row(
                  children: [
                    const Icon(Icons.attach_money, size: 18, color: Colors.green),
                    const SizedBox(width: 4),
                    Text(formatMoney(campaign.budget)),
                    const SizedBox(width: 16),
                    const Icon(Icons.schedule, size: 18, color: Colors.blueGrey),
                    const SizedBox(width: 4),
                    Text(formatShortDate(campaign.deadlineIso)),
                  ],
                ),
                const SizedBox(height: 8),
                Wrap(spacing: 6, children: campaign.tags.map((t) => Chip(label: Text(t))).toList()),
                const SizedBox(height: 8),
                Text(
                  campaign.description,
                  maxLines: 2,
                  overflow: TextOverflow.ellipsis,
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
