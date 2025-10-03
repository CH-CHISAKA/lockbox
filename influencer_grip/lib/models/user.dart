class AppUser {
  const AppUser({
    required this.id,
    required this.fullName,
    required this.username,
    required this.avatarUrl,
    required this.bio,
    required this.followers,
    required this.following,
  });

  final String id;
  final String fullName;
  final String username;
  final String avatarUrl;
  final String bio;
  final int followers;
  final int following;
}
