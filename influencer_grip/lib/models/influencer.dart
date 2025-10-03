class InfluencerProfile {
  const InfluencerProfile({
    required this.id,
    required this.name,
    required this.username,
    required this.avatarUrl,
    required this.categories,
    required this.reach,
    required this.engagementRate,
    required this.ratePerPost,
  });

  final String id;
  final String name;
  final String username;
  final String avatarUrl;
  final List<String> categories;
  final int reach;
  final double engagementRate; // 0..1
  final double ratePerPost; // USD
}
